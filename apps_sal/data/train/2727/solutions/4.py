from collections import Counter

def missing_alphabets(s):
    a, C = [], []
    count = Counter(s)
    
    for i in range(1,max(count.values()) + 1):
        a.append([k for k,v in list(count.items()) if v >= i ])
    

    A = "abcdefghijklmnopqrstuvwxyz"
    B = [I for I in A if I not in s]
    

    for i in range(0 ,len(a)):
        C.append([I for I in A if I not in a[i]])

    return ''.join(sorted([j for i in C for j in i])) 

