n = int(input())
count = [0 for i in range(7)]
for i in range(n):
    s = input()
    l = list(s)
    for j in range(len(l)):
        count[j] += int(l[j])
print((max(count)))
