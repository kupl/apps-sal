def disarium_number(number):
    x=sum(int(d)**(i+1) for i,d in enumerate(str(number)))
    return 'Disarium !!' if number==x else 'Not !!'
