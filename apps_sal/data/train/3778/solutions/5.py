import sys

def find_smallest_int(arr):
    my_int = sys.maxsize
    for integer in arr:
        if integer < my_int:
            my_int = integer
    return my_int
