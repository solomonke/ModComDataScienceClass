# message1 = "This is Python"
# print(message1[1:6])

cars = ["Toyota", "Mazda", "Land Rover", "Mercedes", "Range Rover", "Nissan"]
print(cars)
print(type(cars))
print(cars[2:])

# Tuples

fruits = ("apples", "mangoes", "pears", "melon", "oranges", "avocados", "bananas")
print(fruits)
print(type(fruits))

# slicing
# Lists use square brackets. Tuples use brackets to surround items.

print(fruits[2:4])
print(fruits[0])
print(fruits[-2])
print(fruits[-2:])

# In terms of functionality, tuples cannot be updated. Tuples are immutable.
# Lists are mutable: can be updates.

cars.append("Volkswagen")
cars.remove("Mazda")
cars.insert(0, "Harrier")  # inserts at specified position
print(cars)
