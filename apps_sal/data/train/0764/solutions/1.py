# cook your dish here
n = int(input())
l = []
for i in range(0, n):
    s1 = list(map(str, input().split()))
    s2 = list(map(str, input().split()))
    count = 0
    for j in range(len(s1)):
        if(s1[j] in s2):
            count += 1
    total = len(s1) / 2
    if(count >= total):
        l.append("similar")
    else:
        l.append("dissimilar")
for i in l:
    print(i)
