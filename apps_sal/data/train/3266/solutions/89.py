def my_first_kata(a, b):
    print(a, b)
    try:
        return a % b + b % a
    except:
        return False
