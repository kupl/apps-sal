# cook your dish here
N = int(input())
list1 = list(map(int, input().split()))
nextint = [0 for i in range(N)]
notnext = [0 for i in range(N)]
notnext[-1] = list1[-1]
nextint[-1] = list1[-1]
notnext[-2] = list1[-2]
nextint[-2] = list1[-2] + list1[-1]
for j in range(len(list1) - 3, -1, -1):
    nextint[j] = max(list1[j] + notnext[j + 1], nextint[j + 1])
    notnext[j] = list1[j] + max(nextint[j + 2], notnext[j + 2])
#print("nextint: ",nextint,"notnext: ",notnext)
print(max(nextint[0], notnext[0]))
