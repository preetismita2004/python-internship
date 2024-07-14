class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        #print the result
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I identify as {self.gender}.")

# take input
name_input = input("Enter your name: ")
age_input = int(input("Enter your age: "))
gender_input = input("Enter your gender: ")

# create a person object
person1 = Person(name_input, age_input, gender_input)
person1.introduce()
