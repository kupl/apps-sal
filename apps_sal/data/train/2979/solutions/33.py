def get_age(age):
    newlist = age.split()
    print(newlist)
    numbers = "0","1","2","3","4","5","6","7","8","9"
    age = []
    for i in newlist:
        for x in numbers:
            if i == x:
                age.append(i)
    final = int("".join(age))
    return final
        
get_age("5 years old")
