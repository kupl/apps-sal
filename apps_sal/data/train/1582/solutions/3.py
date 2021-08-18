
n = int(input())
df = str(input())
df = list(df)
ans = 0
l = len(df)
i = 1
while(l > 1):
    if(i < len(df) - 1):
        if(df[i - 1] == df[i]):
            df.pop(i)
            l -= 1
            ans += 1
        else:
            i += 1
    else:
        break
l = len(df)
if(l > 1):
    if(df[l - 1] == df[l - 2]):
        ans += 1
print(ans)
