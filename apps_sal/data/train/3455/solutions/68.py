def disarium_number(number):
    sum1=[]
    for i,v in enumerate(str(number),1):
        sum1.append(pow(int(v),i))
    return 'Disarium !!' if sum(sum1)==number else 'Not !!'
