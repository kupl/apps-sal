from collections import Counter
t=int(input())
for i in range(t):
    a=input()
    b=input()
    print(len(a) - sum((Counter(a) - Counter(b)).values()))
