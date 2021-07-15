t=int(input())
while t>0 :
    t-=1
    s=input()
    d=dict()
    for i in range(0,len(s)-1) :
        word=s[i:i+2]
        d[word]=d.get(word,0)+1
    print(len(d))

