n, m, val = list(map(int, input().split()))

fenwick = [0] * (n + 1)


def add(idx, val):
    while idx <= n:
        fenwick[idx] += val
        idx += idx & -idx


def interval_add(xxx_todo_changeme):
    (right, left, val) = xxx_todo_changeme
    add(right, val)
    add(left + 1, -val)


def val_at(idx):
    ret = 0
    while idx:
        ret += fenwick[idx]
        idx -= idx & -idx
    return ret + val


for _ in range(m):
    q = input().split()
    if q[0] == 'Q':
        print(val_at(int(q[1])))
    else:
        interval_add(list(map(int, q[1:])))
