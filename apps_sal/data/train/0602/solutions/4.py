l = input().split()
mins = l[0]
for s in l:
    if len(s) < len(mins):
        mins = s
ans = mins
for s in l:
    ans += " " + s + " " + mins
print(ans)
