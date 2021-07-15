def my_first_kata(a,b):
    return set(map(type, (a,b))) == {int} and a % b + b % a
