def people_with_age_drink(age):
    dic = {tuple(range(0,14)):"drink toddy", tuple(range(14,18)):"drink coke", tuple(range(18,21)):"drink beer"}
    return  dic.get(max(i if age in i else (0,0) for i in dic), "drink whisky") 
 

