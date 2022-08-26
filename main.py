professions = {
            "DVL":"Developer",
            "MNG":"Manager",
            "QA":"Quality assurance",
            "MRG":"Marketing",
            "HR":"Human resources",
        }

firstName = input("Enter your First Name:")
lastName = input("Enter your Last Name:")
age = input("Enter your age:")
profession = input("MNG,DVL,QA,MRG,HR:")
class Person:
    def __init__(self,firstName,lastName,age,profession):
        self.firstName = firstName 
        self.lastName = lastName
        self.age = age
        self.profession = professions[profession]

people = Person(firstName,lastName,age,profession)
peoples = []
peoples.append(people)

def my_function():
    filterPeoples = []
    for item in peoples:
        if item.firstName == "Vazgen" and item.age < "25" and item.profession == "Developer":
            filterPeoples.append(item)
        else:
            print("Error")

my_function()