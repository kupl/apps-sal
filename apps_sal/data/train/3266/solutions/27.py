def my_first_kata(a, b):
    print(type(a))
    print(type(b))
    print(a)
    print(b)
    try:
        print(a % b + b % a)
        return a % b + b % a
    except (TypeError, ZeroDivisionError):
        return False
