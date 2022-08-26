from data import professions
from data import peoples
from data import filterPeoples
class Person:
    def __init__(self,firstName,lastName,age,profession):
        self.firstName = firstName 
        self.lastName = lastName
        self.age = age
        self.profession = professions[profession]

def my_function():
    firstName = input("Enter your First Name:")
    lastName = input("Enter your Last Name:")
    age = int(input("Enter your age:"))
    profession = input("MNG,DVL,QA,MRG,HR:")
    people = Person(firstName,lastName,age,profession)
    peoples.append(people)
    for item in peoples:
        if item.firstName == "Vazgen" and item.age < 25 and item.profession == "Developer":
            filterPeoples.append(item)
            peoples.remove(item)
        else:
            print("Error with user")
while 1:
    my_function()