def subseq(s, b):
    h = iter(b)
    return all((any((l == ch for l in h)) for ch in s))


t = input()
p = input()
num = [int(x) for x in input().split()]
st = []
l = 0
r = len(num)
ans = r + 1
while l <= r:
    mid = (l + r) // 2
    st = list(t)
    c = num[:mid]
    for i in c:
        st[i - 1] = ''
    if subseq(p, ''.join(st)):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
