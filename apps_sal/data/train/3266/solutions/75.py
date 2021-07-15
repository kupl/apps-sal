def my_first_kata(a,b):
    # Tricky 
    if type(a) != type(b):
        return False
    else:
        return int(b % a) + int(a % b)
    

