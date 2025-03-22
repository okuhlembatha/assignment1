num1 = float(input("enter your 1st number:"))
num2 = float(input("enter yoye 2nd number:"))

sign = input("choose a mathematical sign (add, subtract, multiply, divide)")

if sign == "add":
    answer = num1 + num2
elif sign == "subtract":
    answer = num1-num2
elif sign == "multiply":
    answer = num1*num2
elif sign == "divide":
    if num2 !=0:
        answer = num1/num2
    else:
        answer = "undefined."

print("The answer is:", answer)

