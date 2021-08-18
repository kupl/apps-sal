def my_add(a, b):
    try:
        return a + b
    except TypeError:
        print("None")
