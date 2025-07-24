#Data structures
fruits = ["apple", "cherry", "banana"]
print(fruits[0])

fruits[1] = "blueberry"
print(fruits)

#add items

fruits.append("pear")
print(fruits)

fruits.insert(1, "orange")
print(fruits)

#remove items

fruits.remove("pear")
print(fruits)

#sort lists
#sort() - ascending order
#sort(reverse=True) - descending order
fruits.sort(reverse=True) 
print(fruits)