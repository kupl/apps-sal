def disarium_number(number):
    a=0
    for j,i in enumerate(str(number)):
        a+=int(i)**(j+1)
    return 'Disarium !!' if a==number else 'Not !!'

