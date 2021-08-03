def dating_range(age):
    return f'''{int(age/2+7)}-{int(age*2-7*2)}''' if age > 14 else f'''{int(0.9*age)}-{int(1.1*age)}'''
