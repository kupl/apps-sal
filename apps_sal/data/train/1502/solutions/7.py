for _ in range(int(input())):
    s=input().strip()
    n=int(input())
    l=list(input())
    f=0
    for i in range(len(s)):
        if s[i] not in l:
            f=1
            break
    if f==1:
        print(0)
    else:
        print(1)

