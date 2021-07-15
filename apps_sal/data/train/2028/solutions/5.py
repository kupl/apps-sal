import sys
string=input()
n=len(string)
c=string[0]
if all(c==string[i] for i in range(n//2)) and all(c==string[i] for i in range((n+1)//2,n)):
    print("Impossible")
    return

for i in range(1,n):
    part=string[i:]+string[:i]
    if part==part[::-1] and part!=string:
        print(1)
        return
print(2)

