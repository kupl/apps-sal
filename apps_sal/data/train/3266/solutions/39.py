def my_first_kata(a,b):
    if type(a) == str:
        return False
    if type(b) == str: 
        return False
    else:
        return a % b ++ b % a
