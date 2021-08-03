def my_first_kata(a, b):
    return all(type(x) == int for x in (a, b)) and (a % b) + (b % a)
