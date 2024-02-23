Current_year = 2024
yob = float(input("YOB => "))
Age = Current_year - yob
if((Age<18) and (Age>0)):
    print ( " You are " , Age , "years old" )
    print("Sorry you are too young hence inelligible for this service")
elif(yob<1900):
    print("Please enter valid date of birth")
elif(Age<0):
    print("wacha ufala")
else:
    print ( " You are " , Age , "years old" )
    print("you are of age hence elligible for this service welcome")
