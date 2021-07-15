# given a number, 0 <= n <=9, return it in words
# input - number as integer
# output - string
# edge cases - decimals/floats, invalid input

# sample data - 8 = "Eight"
# how does a computer convert from integer to string

def switch_it_up(number):
    words = {0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine"
    }
    return words.get(number)
