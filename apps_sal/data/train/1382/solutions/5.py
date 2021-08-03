
n = int(input())
a = list(map(int, input().split()))
x = int(input())
l1 = [i for i in a if i < 0]
l1.sort()
l1.reverse()
if(len(l1) > x and x > 0):
    i = len(l1) - x
    l2 = l1[0:i]
    l1 = l1[i:]
    cnt1 = abs(sum(l2)) * x - abs(sum(l2[0:i - 1]) * x)
    cnt2 = abs(sum(l1)) - ((cnt1 // x) * len(l1))
    cnt = cnt1 + cnt2
    print(cnt)
elif(x == 0):
    print(0)
else:
    print(abs(sum(l1)))
