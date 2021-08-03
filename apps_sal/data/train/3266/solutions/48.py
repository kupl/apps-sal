def my_first_kata(a, b):
    if any([t not in ['int', 'float'] for t in (type(a).__name__, type(b).__name__)]):
        return False
    else:
        return a % b + b % a
