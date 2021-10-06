# Day 16: Exceptions - String to Integer


s = input()
try:
    int_convert = int(s)
    print(int_convert)
except ValueError:
    print("Bad String")
