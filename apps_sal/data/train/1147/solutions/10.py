for _ in range(int(input())):
    n=int(input())
    s=input()
    if s==s[::-1]:
        print(0)
    else:
        an=0
        ar=[0]*26
        for i in range(n):
            ar[ord(s[i])-97]+=1
        for i in range(26):
            if ar[i]%2!=0:
                an+=1
        if an==0:
            print(0)
        else:
            print(an-1)

