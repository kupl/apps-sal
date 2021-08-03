s, k = map(int, input().split())
i = 0
c = 0
st = list(str(s))
while(i < k):
    if i >= len(st):
        break
    if st[i] != "9":
        st[i] = "9"
        c = c + 1
    i = i + 1
if c < k:
    for i in range(len(st)):
        if c >= k:
            break
        if st[i] != '9':
            st[i] = '9'
            c = c + 1
st = "".join(st)
s = int(st)
print(s)
