# cook your dish here
import copy
N = int(input())
list1 = list(map(int,input().split()))
list2 = copy.deepcopy(list1)
for i in range(len(list1)-3,-1,-1):
    list1[i] += min(list1[i+1],list1[i+2])
for j in range(2,len(list2)):
    list2[j] += min(list2[j-1],list2[j-2])
answer = min(list1[0], list2[-1])
#print(list1,list2)
print(answer)
