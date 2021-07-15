 
import sys
input=sys.stdin.readline
for j in range(int(input())):
    a = input()
    a = a + 'R'
    ans = 1
    count =0
    for j in a:
        if(j=='L'):
            count= count + 1
        else:
            count = count + 1
            if(count>ans):
                ans = count
            count = 0
    print(ans)
            

