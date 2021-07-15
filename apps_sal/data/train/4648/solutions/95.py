def automorphic(n):
    num=list(map(int, str(n**2)))
    num=num[::-1]
    num2=list(map(int, str(n)))
    num2=num2[::-1]
    for i in range(len(num2)):    
        if num2[i]==num[i]:
            continue
        else:
            return "Not!!"
    return "Automorphic"
