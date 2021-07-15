def disarium_number(number):
    return ('Not','Disarium')[number == sum(int(d)**i for i,d in enumerate(str(number),1))] + ' !!'
