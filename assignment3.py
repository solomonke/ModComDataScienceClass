# In this Python Lesson, we will learn how to find if a year is a
# leap year or not in Python.
# Leap Year (LY) is a year which satisfies the following conditions:
# •The year should be divisible by 4.
# •The year should be divisible by 4 and not divisible by 100.
# •The Year should divisible by 4, and divisible 400


years = [1990, 2000, 1968, 2022, 1997, 2010, 1988, 2008, 2004, 2001]
leap_year = []

# for x in years:
#     if x % 4 == 0 and x % 400 and 100 != 0:
#         leap_year.append(x)
#     print(leap_year)

for x in years:
    if x % 4 == 0:
        leap_year.append(x)
        if x % 100 != 0 and x % 400 == 0:
            leap_year.append(x)
    print(leap_year)




