t = int(input())
while(t!=0):
    t-=1
    string = input()
    s = []
    for i in range(len(string)):
        s.append(int(string[i]))
    
    sqinc = 0
    for i in range(1,len(s)):
        if s[i-1]!=s[i] and s[i-1] == 1:
            sqinc+=1
        if s[i-1]!=s[i] and s[i-1]==0:
            break
        if s[i-1]==s[i] and s[i-1]==0 and sqinc>0:
            sqinc+=1
    print(sqinc)


