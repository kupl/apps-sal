
import heapq as hp
from sys import stdin
testCases = int(input())
result=[]
while testCases:
    try:
        number= int(input())
        team_A = [int(x) for x in input().split()]
        team_B = [int(x) for x in input().split()]
        if max(team_A)!=max(team_B):
            result.append("YES")
        else:
            result.append("NO")
    
        testCases=-1
    except:
        break
for i in result:
    print(i)
