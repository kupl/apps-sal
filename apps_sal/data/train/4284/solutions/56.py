def array_leaders(numbers):
    if len(numbers)<3:
       return numbers
    n=[]
    for i in range(len(numbers)):
        if int(numbers[i])>sum(numbers[i+1:]):
           n.append(numbers[i])
    return n
