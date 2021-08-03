want = input()
n = int(input())
l = [input() for _ in range(n)]
works = False
if want in l:
    works = True
for i in range(n):
    for j in range(n):
        if want in l[i] + l[j]:
            works = True

print("YES" if works else "NO")
