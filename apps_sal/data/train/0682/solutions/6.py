n = int(input())
x = [int(x) for x in input().split()]
np = [int(np) for np in range(1, n + 1)]
l = []
for i in range(len(x)):
    if(x[i] != np[i]):
        l.append(i)
if(len(l) > 0):
    # print(''.join(map(str,list(reversed(x[min(l):max(l)+1])))),''.join(map(str, np[min(l):max(l)+1])))
    if(''.join(map(str, list(reversed(x[min(l):max(l) + 1])))) == ''.join(map(str, np[min(l):max(l) + 1]))):
        print(min(l) + 1, max(l) + 1)
    else:
        print("0 0")
else:
    print("0 0")
