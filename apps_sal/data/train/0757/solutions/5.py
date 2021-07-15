vowels=['a','e','i','o','u']
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    s=s.lower()
    flag=0
    for i in range(len(s)):
        if(s[i] in vowels and s[(i+1)%n] in vowels):
            flag=1
            break
    if(flag==1 and n>1):print("Yes")
    else:print("No")

