def grader(score):

    result="F"
    if score>=0.6 and score <0.7:
       result="D"
    elif score>=0.7 and score <0.8:
       result="C"  
    elif score>=0.8 and score <0.9:
       result="B" 
    elif score>=0.9 and score <=1.0:
       result="A" 
    else:
       result="F"
       
    return result   

