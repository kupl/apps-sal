def array_leaders(numbers):
    i=len(numbers)-1
    tot=0
    ans=[]
    while i>=0:
        if numbers[i]>tot:
            ans.append(numbers[i])
        tot=tot+numbers[i]
        i=i-1
    return ans[::-1]
