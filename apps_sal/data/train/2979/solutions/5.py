def get_age(age):
    age=age[0]#select the first element of the string
    age=int(age)#cause age is a char, we need to convert in to a integer 
    if age>9 or age<0:
        return 0
    else:
        return age
