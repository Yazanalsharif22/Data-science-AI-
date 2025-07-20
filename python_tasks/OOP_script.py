print(
    "########################################################################################################################"
)
print("Task 1 : ")
print()


# Task 1
class Shape:

    def area(self):
        return 0

    def print_info(self):
        print("Default Shape")


class Rectangle(Shape):

    def __init__(self, width: float = 0, hight: float = 0):
        # super().__init__()
        self.width = width
        self.hight = hight

    def area(self) -> float:
        return self.width * self.hight

    def print_info(self):
        print("Rectangle Shape")


class Circle(Shape):
    def __init__(self, width):
        # super().__init__()
        self.width = width
        self.Pi = 3.14

    def area(self):
        return self.width * self.Pi

    def print_info(self):
        print("Circle Shape")


# create Shape object
shape = Shape()
print(f"Shape area = {shape.area()}")
# create Rectangle object
rect = Rectangle(5, 6)
print(f"Rectangle area = {rect.area()}")

# create Circle object
circle = Circle(10)
print(f"Circle area = {circle.area():.2f}")

print()
print(
    "########################################################################################################################"
)
print("Task 2 : ")
print()

# Task 2
# Print the type of shape
shape.print_info()
rect.print_info()
circle.print_info()
print()
print(
    "########################################################################################################################"
)
print("Task 3 : ")
print()


# Task 3
class BankAccount:

    def __init__(self, account_number: str = "", balance: float = 0):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self) -> str:
        return self.__account_number

    def get_balance(self) -> str:
        return self.__balance

    def deposit(self, dep: float):
        self.__balance += dep

    def withdraw(self, withd: float):
        if self.__balance - withd <= 0:
            return False
        else:
            self.__balance -= withd
            return True


print("Case 1 : ")
account = BankAccount("54542858", 10000)

print(f"Account Number : {account.get_account_number()}")

print(f"Balanc : {account.get_balance()}")

account.deposit(17500)
print(f"Balanc After Deposit : {account.get_balance()}")

check = account.withdraw(7500)
if check:
    print(f"Balanc After Withdraw : {account.get_balance()}\n")
else:
    print(f"Ther is no enough money to withdraw")


print("Case 2 : ")
account = BankAccount("25456873", 14000)

print(f"Account Number : {account.get_account_number()}")

print(f"Balanc : {account.get_balance()}")

account.deposit(17500)
print(f"Balanc After Deposit : {account.get_balance()}")

check = account.withdraw(37500)
if check:
    print(f"Balanc After Withdraw : {account.get_balance()}")
else:
    print(f"Ther is no enough money to withdraw")

print()
print(
    "########################################################################################################################"
)
print("Task 4 : ")
print()


# Task 4
class Animal:

    def speak(slef):
        print("I don't Know what I say!")


class Dog(Animal):

    def speak(self):
        print("Woof Woof!")


class Cat(Animal):

    def speak(self):
        print("Meow Meow!")


animal = Animal()
animal.speak()
print()
dog = Dog()
dog.speak()
print()
cat = Cat()
cat.speak()

print()
print(
    "########################################################################################################################"
)
print("Task 5 : ")
print()


# Task 5
def animal_speak(a):
    a.speak()


animal_speak(animal)
animal_speak(dog)
animal_speak(cat)


class Car:
    def __init__(self, color: str = "", speed: int = 0):
        self.color = color
        self.__speed = speed

    def accelerate(self):
        self.__speed += 10

    def get_speed(self) -> int:
        return self.__speed


print()
print(
    "########################################################################################################################"
)
print("Task 6 : ")
print()


car = Car("black", 90)

print(f"The Current Car Speed : {car.get_speed()}")

car.accelerate()
print(f"The Car Speed after increasing acceleration : {car.get_speed()}")
