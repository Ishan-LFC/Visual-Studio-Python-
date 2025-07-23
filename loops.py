#loops

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 5, 7] #be careful with spacing, it chnages the iteration
#space kept between numbers and for loop, test to see difference
for number in numbers:
    print(numbers)


#while loop
count = 1

while count <=5:
    print(count)
    count+=1 #increment
    
#loops part 2
fruits2 = ["pear", "apple", "berry", "date"]

for fruit1 in fruits2:
    if fruit1 == "berry":
      break #exits loop if berry found
    print(fruit1)
    
print()

for fruit1 in fruits2:
    if fruit1 == "berry":
      continue #skips cherry and moves iteration
    print(fruit1)
    
print()

for fruit1 in fruits2:
    if fruit1 == "berry":
      pass #placeholder, no action is needed for berry
    print(fruit1)
    
    #loops continued
    
    count = 0
    
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break #exits loop when the count is reached
    
#BE VERY CAREFUL WITH SPACING, ALL LOOPS NEED TO BE IN LINE ELSE YOU'LL HVE WHILE LOOPS IN FOR LOOPS ETC....