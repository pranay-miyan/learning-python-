

while True:
    try:
        num = int(input("What is your digits! : "))
        num2 = int(input("What is your second digit! : "))
    except ValueError:
        print("Please enter correctly!")
        
        symbol = input("What operation do you want? - (*, / , + , -) : ")
        if symbol == "*":
            print(f"Your answer is {num*num2}.")
            break
        elif symbol == "+":
            print(f"Your answer is {num+num2}.")
            break
        elif symbol == "-":
            print(f"Your answer is {num-num2}.")
            break
        elif symbol == "/":
            print(f"Your answer is {num/num2}.")
            break
        else:
            print("Please choose from:(/, +, -, *)")

