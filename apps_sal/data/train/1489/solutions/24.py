s, k = [int(s) for s in input().split(" ")]
a = str(s)
ans = ""
for ch in a:
    if k > 0:
        if int(ch) < 9:
            ans += "9"
            k-=1
        else:
            ans += ch
    else:
        ans += ch
print(ans)

