def dating_range(age):
    return ['%d-%d'%(age-.10*age, age+.10*age), '%d-%d'%(age/2+7, (age-7)*2)][age>14]
