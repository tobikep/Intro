first = float(input("Enter first number => "))
sec = float(input("Enter second number => "))
opr = str(input("Enter Operative(+, -, *, /) => "))

if opr =="+":
    total = first + sec
elif opr =="-":
    total = first - sec
elif opr =="*":
    total = first * sec
elif opr =="/":
    total = first / sec
else:
    total = str("Please enter valid operatives")

print ( total )
