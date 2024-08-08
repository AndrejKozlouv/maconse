class Mammal:
    def __init__(self, name, age, num_legs):
        self.name = name
        self.age = age
        self.num_legs = num_legs

    def __str__(self):
        return f"{self.name} is {self.age} years old and has {self.num_legs} legs."

# Create an instance of Mammal
tiger = Mammal('Tiger', 5, 4)

# Print out information about the tiger
print(tiger)
