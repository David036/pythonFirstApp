professions = {
            "profession1":"Developer",
            "profession2":"Manager",
            "profession3":"QA",
            "profession4":"Marketing",
            "profession5":"HR",
        }

class Person:
    def __init__(self,firstName,lastName,age,profession):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.profession = professions[profession]


people1 = Person("Vazgen","Yan",26,"profession2")
people2 = Person("Vazgen","YanYan",23,"profession1")
people3 = Person("KKKKK","Yan",30,"profession1")
people3 = Person("Vazgen","Yan",20,"profession2")

peoples = [people1,people2,people3]


def my_function():
    filterPeoples = []
    for item in peoples:
        if item.firstName == "Vazgen" and item.age < 25 and item.profession == "Developer":
            filterPeoples.append(item)

my_function()