def get_age(age):
    #your code here
    for item in age:
        if item.isnumeric():
            return int(item)
