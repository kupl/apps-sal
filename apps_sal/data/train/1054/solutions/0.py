test=int(input())
for i in range(test):
    s=input()
    b=len(s)
    list1=[]
    for j in range(len(s)):
        if s[j]=='.':
            list1.append(j)
    for i in list1:
        if b-i-1 in list1 :
            if i!=b-i-1 and ((s[i] and s[b-i-1]) != 'a' ):
                s=s[:i]+'a'+s[i+1:b-i-1]+'a'+s[b-i:]
            else:
                s=s[:i]+'a'+s[i+1:]
        else:
            s=s[:i]+s[b-i-1]+s[i+1:]

    if s==s[::-1]:
        print(s)
    else:
        print(-1)

        
