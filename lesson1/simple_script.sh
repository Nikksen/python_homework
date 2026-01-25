#!/bin/bash

echo "Enter your name:"
read name

echo "Hi, $name"
echo "How old are you ?"
read age   
year=$((2026 - age)) 
echo "So year of your birth is: $year"

while true; do
    echo "Do you wanna calculate something ? (Yes / No)"
    read answer
        if [ "$answer" = "Yes" ]; then
            echo "Choose operation:"
            echo "1. Add"
            echo "2. Subtract"
            echo "Your choice 1 or 2"
            read choice
        if [ $choice -eq 1 ]; then
            read -p "Enter first number: " num1
            read -p "Enter second number: " num2
            result=$((num1 + num2))
            echo "Result: $num1 + $num2 = $result"
        elif [ $choice -eq 2 ]; then
            read -p "Enter first number: " num1
            read -p "Enter second number: " num2
            echo "Result: $num1 - $num2 = $result"           
        else
            "Incorrect option"
        fi    
    else
        echo "Bye, $name"
        break
    fi        
done