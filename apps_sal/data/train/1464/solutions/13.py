from sys import stdin, stdout
ans = []


def leap_check(yy):
    if yy % 400 == 0:
        return True
    elif yy % 100 == 0:
        return False
    elif yy % 4 == 0:
        return True
    else:
        return 0


for _ in range(int(stdin.readline())):
    yy, mm, dd = list(map(int, stdin.readline().split(':')))
    if mm in [1, 3, 5, 7, 8, 10, 12]:
        ans.append(str(int(((31 - dd) / 2) + 1)))
    elif mm in [4, 6, 9, 11]:
        ans.append(str(int(((30 - dd) / 2) + 16 + (dd % 2))))
    else:
        ans.append(str(int((29 - dd) / 2 + 1)
                       if leap_check(yy) else int((28 - dd) / 2 + 16 + (dd % 2))))
stdout.write('\n'.join(ans))
