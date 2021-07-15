def calculator(x,y,op):
    if isinstance(x,int)==False:
        return "unknown value"
    elif isinstance(y,int)==False:
          return "unknown value"
    elif str(op)=="+":
         return x+y
    elif str(op)=="-":
        return x-y
    elif str(op)=="/":
        return x/y
    elif str(op)=="*":
        return x*y
    else:
        return "unknown value"
