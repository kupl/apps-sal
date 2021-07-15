try:
    t=int(input())
    for _ in range(t):
        s=list(input())
        i=0
        le=len(s)
        while(i<le-2):
            if i<0:
                i=0
            if le<3:
                break
            if s[i]=="a" and s[i+1]=="b" and s[i+2]=="c":
                s.pop(i)
                s.pop(i)
                s.pop(i)
                i-=3
                le-=3
                continue
            i+=1
        for ch in s:
            print(ch,end="")
        print()
except EOFError:
    pass
