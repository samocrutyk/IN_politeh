class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("person created")

    def say_age(self):
        print(f"{self.name} is {self.age} age")

p1 = Person("tom", 17)
p1.say_age()
class Men(Person):
    pass
class Women(Person):
    pass

m1 = Men("Alex", 47)
w1 = Women("Olga", 34)

m1.say_age()
w1.say_age()