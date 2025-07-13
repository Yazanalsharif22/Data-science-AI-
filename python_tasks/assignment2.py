print("###########################################################")
print("TASk 1")
# input var.
name = input("Enter Your Name: ")
fav_food = input("Enter Your Favorite Food: ")
print("{" + f"{name}" + "} " + "Likes " + "{" + f"{fav_food}" + "}")

print("###########################################################")
print("TASk 2")

print(help(list))
# we use append method  to add elemnet at end of list
# print("Discripe append method")
# print(help(list.append))


print("###########################################################")
print("TASk 3")

price = "123$"
price = price.replace("$", "")
a = int(price)  # covert string to integer
a += 100
price = str(a) + "$"  # covert integer to string
print(price)


print("###########################################################")
print("TASk 4")

num = int(input("Enter The Number: "))

if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is exactly zero")
else:
    print("Number is Negative")
