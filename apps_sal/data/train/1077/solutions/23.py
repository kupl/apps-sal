T = int(input())
for i in range(T):
    N = int(input())
    strs = []
    for j in range(N):
        strs.append(input())
    strs = list(reversed(strs))
    prev = None
    for index, direction in enumerate(strs):
        if index == 0:
            s = direction.split()
            print('Begin ' + ' '. join(s[1:]))
            prev = direction
            continue
        if prev.startswith('Left'):
            print('Right ' + ' '. join(direction.split()[1:]))
        else:
            print('Left ' + ' '. join(direction.split()[1:]))
        prev = direction
