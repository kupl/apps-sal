N = int(input())
Alist = list(map(int, input().split()))
XorPro = 0
for i in Alist:
    XorPro = XorPro ^ i
Answer = []
for i in Alist:
    Answer.append(XorPro ^ i)
print(*Answer)
