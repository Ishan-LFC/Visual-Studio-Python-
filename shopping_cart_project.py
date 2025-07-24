#project

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to Quit ")
    if food.lower() == 'q' :
        break
    else :
        price = float(input(f"Enter the price of the product{food}: R"))
        foods.append(food)
        prices.append(price)

print("------ Your Cart -------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print("\n")
print(f"Your total is: R{total}" )