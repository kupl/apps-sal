# cook your dish here
possiblity = {'?EHC', '??H?', '?E??', '?EH?', 'F?H?', '???C', '?E?C', 'FE?C',
              'F???', 'FE??', '????', 'FEH?', '??HC', 'F??C', 'F?HC'}
for _ in range(int(input())):
    st = input()
    st = st[::-1]
    ln = len(st)
    ans = ['0'] * ln
    i = ln - 1
    i = 0
    while i + 3 < ln:
        if st[i:i + 4] in possiblity:
            ans[i:i + 4] = ['F', 'E', 'H', 'C']
            i += 4
        else:
            ans[i] = st[i]
            i += 1
    if i < len(st):
        ans[i:] = st[i:]
    for i in range(ln):
        if ans[i] == '?':
            ans[i] = 'A'
    print(*ans[::-1], sep='')
