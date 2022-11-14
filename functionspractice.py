# functions

def func1():
    print("This is a good programming language.")


# referencing/invoke/call
func1()


def multiply(x, y):
    answer = x * y
    print("X multiplied by Y is: ", answer)


multiply(4, 6)


# Write a function to find simple interest Simple Interest = Principal x Interest Rate x Time

def simple_interest(p, r, t):
    answer = (p * r * t) / 100
    print("Simple interest is: ", answer)


simple_interest(10000, 13, 5)
