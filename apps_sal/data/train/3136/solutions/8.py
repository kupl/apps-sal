def people_with_age_drink(age):
    drinks = {1:'drink toddy',2:'drink coke',3:'drink beer',4:'drink whisky'}
    return drinks[1] if age<14 else drinks[2] if age<18 else drinks[3] if age<21 else drinks[4]
