a = list(map(int, input().split()))
out = 'Impossible'
for i in range(4):
    if out == 'Possible':
        break
    for j in range(1, 4):
        (a[i], a[j]) = (a[j], a[i])
        if a[0] / a[1] == a[2] / a[3]:
            out = 'Possible'
            break
        else:
            (a[i], a[j]) = (a[j], a[i])
print(out)
