#control statements

num = 0

if num > 0:
    print("this number is positive") #must leave a space before print
elif num == 0:
    print("the number is zero") 
else:
    print("this number is negative")
    

#part 2
num1 = int(input("Enter the first numnber:"))
num2 = int(input("Enter the second numnber:"))

if num1 > num2:
 print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("both numbers are equal")