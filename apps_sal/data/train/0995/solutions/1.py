# cook your dish here
ld = {}
rd = {}
n = int(input())
l = list(map(int, input().split()))
k = int(input())
l1 = []
l2 = l[::-1]
t = k

while(k):
    l1.append(sum(l[:k]) + sum(l2[0:t - k]))
    # print(l1)
    k -= 1
l1.append(sum(l2[:t]))
print(max(l1))
