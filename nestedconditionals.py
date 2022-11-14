# Nested Conditionals

points = int(input("Your Points: "))
age = int(input("Your age: "))

if points < 50:
    print("Not eligible for the trip")
elif 50 <= points <= 75:
    print("We will consider a prize.")
else:
    print("You will be considered for the trip.")
    if age <10:
        print("You're going to Disneyland!")
    else:
        print("You will visit KenGen for an educational tour.")