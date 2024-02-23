No_of_nos = float(input("Enter amount of numbers to be computed => "))
i = 0
sum = 0
while i < No_of_nos:
    Number = float(input("Please enter a new number => "))
    sum = sum + Number
    i = i + 1
Avg = sum / No_of_nos
print ( "The average value is" , Avg )