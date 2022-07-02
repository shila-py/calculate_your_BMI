# calculator
first_number = float(input("please enter one number: "))
second_number = float(input("please enter second number: "))
char = input(" please enter one of these characters : (+ - * / % // ** ) :  ")

if char == "+":
    print(first_number + second_number)

elif char == "-":
    print(first_number - second_number)

elif char == "*":
    print(first_number * second_number)

elif char == "/":
    print(first_number / second_number)

elif char == "%":
    print(first_number % second_number)

elif char == "//":
    print(first_number // second_number)

elif char == "**":
    print(first_number ** second_number)
else:
    print("please try again !!!! ")
