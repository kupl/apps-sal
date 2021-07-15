from math import sqrt

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    sum=0
    sum=age_1*age_1+age_2*age_2+age_3*age_3+age_4*age_4+age_5*age_5+age_6*age_6+age_7*age_7+age_8*age_8
    sum=sqrt(sum)/2
    return int(sum)
