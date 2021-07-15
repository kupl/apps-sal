from functools import reduce

def colorful(n):
    s = list(map(int,str(n)))
    return len(s)*(len(s)+1)//2 == len({ reduce(int.__mul__, s[i:i+x]) for x in range(1,len(s)+1) for i in range(len(s)-x+1)})
