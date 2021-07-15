def array(string):
    length=len(string)
    answer=""
    if length==0 or length==1 or length==3:
        answer=None
    else:
        x=0
        comma=[]
         
        while x<length:
            if string[x]==",":
                comma.append(x)
            x=x+1
        if len(comma)>0:
            start=comma[0]
            stop=comma[-1]
            answer=string[start:stop+1]
            
        answer=answer.replace(',', ' ')
        answer=answer [1:-1]
        if answer=="":
            answer=None
    return answer
