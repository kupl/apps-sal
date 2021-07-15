n = int(input())
l = [int(x) - 1 for x in input().split()]
parity = 0
explore = set(l)
while len(explore) > 0:
    x = explore.pop()
    tmp = x
    found = [x]
    while l[tmp] != x:
        tmp = l[tmp]
        found.append(tmp)
    for i in found[1:]:
        explore.remove(i)
    parity ^= (len(found) - 1) % 2

if parity == n % 2:
    print("Petr")
else:
    print("Um_nik")
