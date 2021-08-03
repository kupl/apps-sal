def my_first_kata(a, b):
    if type(a) == int and type(b) == int:
        return (b % a + a % b)
    else:
        return False
