def answer(question,information):
    info=[ i.split(" ")  for i in information]
    ques=question.lower().split(" ")
    high=0 ; iHigh=-1
    for i in range(len(info)):
        score=0
        for j in info[i]:
            if j.lower() in ques:
                score+=1 
        if score>high:
            iHigh=i
            high=score
    if iHigh==-1:return None
    a="".join(j+" " for j in info[iHigh])[:-1]
    return a
    
        

