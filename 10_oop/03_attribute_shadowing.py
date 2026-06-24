# An attribute is a variable that belongs to an object or class.

# Attribute shadowing happens when an instance attribute has the same name as a class attribute.

class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)