t=int(input().strip())
for i in range(t):
    word=input().strip()
    n=len(word)
    s=n*(n+1)/2
    t7=0
    for j in range(n):
        if word[j]=='7': t7+=1
        else:
            s-=t7*(t7+1)/2
            t7=0
    s-=t7*(t7+1)/2
    print(s)
    

