def get_age(age):
    # your code here
    for c in age:
        if c.isdigit():
            return int(c)
