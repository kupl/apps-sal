test=int(input())
#def solve():
    
'''hile test:
    solve()
    test-=1 '''
count=0
s=input()
for i in range(test-1):
    if s[i+1]==s[i]:
        count+=1 
print(count)

