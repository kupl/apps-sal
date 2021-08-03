# cook your dish here
import itertools
t = int(input())
for i in range(t):
    def subset(num, k):
        return(list(itertools.combinations(num, k)))
    n, k = list(map(int, input().split()))
    num = list(map(int, input().split()))
    y = subset(num, k)
    num1 = []
    for i in range(len(y)):
        num1.append(sum(y[i]))
    x = min(num1)
    print(num1.count(x))
