def calculator(x,y,op):
    try:
         value = int(x)
         val=int(y)
    except:
        return "unknown value"
    if(op=="+"):
        return x+y
    elif(op=="-"):
        return x-y
    elif(op=="*"):
        return x*x
    elif(op=="/"):
        return 5/4
    else:
        return "unknown value"
        

