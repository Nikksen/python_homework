from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method != 'POST':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username or not email or not password:
            return render_template('register.html', error='All fields are required!')

        existing_user_username = User.query.filter_by(
            username=username).first()
        if existing_user_username:
            return render_template('register.html', error="Username already registered!")

        existing_user_email = User.query.filter_by(email=email).first()
        if existing_user_email:
            return render_template('register.html', error="Email already registered!")

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method != 'POST':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return render_template('login.html', error='All fields are required')

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return render_template('login.html', error='Invalid password or email!')

        return f'Welcome back, {user.username}!'
