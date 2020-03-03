class student:
    def __init__(self, name1, age1): #class
        self.name = name1
        self.age = age1

john = student("john", "21")
jane = student("jane", "22") #objects

print(getattr(jane,"age")) #print