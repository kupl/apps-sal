BigNum = 10 ** 20

n, m, a, d = list(map(int, input().split(' ')))
ts = [0] + list(map(int, input().split(' '))) + [BigNum]


def empsInRange(l, r):
    em1 = l // a + 1
    em2 = r // a
    return (em1, min(em2, n))


empDoorGroup = d // a + 1


def moveEmps(emps, last):
    em1, em2 = emps
    if em1 > em2:
        return last, 0

    if em1 * a <= last + d:
        gr1 = (last + d - em1 * a) // a
        em1 += 1 + gr1

    if em1 > em2:
        return last, 0

    doorGroups = (em2 - em1 + 1 + empDoorGroup - 1) // empDoorGroup
    last = (em1 + empDoorGroup * (doorGroups - 1)) * a

    return last, doorGroups


res = 0
last = -BigNum

for i in range(1, len(ts)):
    #print(i, ' ------------ ')
    emps = empsInRange(ts[i - 1], ts[i])
    #print(ts[i-1], ts[i], emps, last)
    last, inc = moveEmps(emps, last)
    #print('last:', last, ' inc:', inc)
    res += inc

    if ts[i] < BigNum and last + d < ts[i]:
        res += 1
        last = ts[i]
    #print('temp res:', res)

print(res)
