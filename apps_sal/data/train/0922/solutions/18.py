# cook your dish here
n = int(input())
res = []
for _ in range(n):
    m = input().split()
    ls1 = list(map(int, input().strip().split()))
    ls2 = list(map(int, input().strip().split()))
    ls1 = set(ls1)
    ls2 = set(ls2)
    c = ls1.intersection(ls2)
    ls1 = list(ls1)
    ls2 = list(ls2)
    for ele in c:
        ls1.remove(ele)
        ls2.remove(ele)
    ls1.extend(ls2)
    ls1.sort()
    for ele in ls1:
        print(ele, end=" ")
