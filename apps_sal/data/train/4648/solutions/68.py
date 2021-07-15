def automorphic(n):
    #print(str(n**2)[(len(str(n))-1):])
    #print(str(n**2)[-1:len(str(n))+1])
    return "Automorphic" if str(n) in str(n**2) else "Not!!"
