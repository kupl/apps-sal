q = int(input())
while q:
    s = input()
    m = {}
    m['D'] = 0
    m['U'] = 0
    m['L'] = 0
    m['R'] = 0
    for i in s:
        m[i] += 1
    k = min(m['D'], m['U'])
    m['D'] = k
    m['U'] = k
    k1 = min(m['L'], m['R'])
    m['L'] = k1
    m['R'] = k1
    if m['D'] == 0:
        m['L'] = min(1, m['L'])
        m['R'] = m['L']
    if m['L'] == 0:
        m['D'] = min(m['D'], 1)
        m['U'] = m['D']

    print(m['L'] + m['D'] + m['R'] + m["U"])
    print('L' * m['L'], end='')
    print('U' * m['U'], end='')
    print('R' * m['R'], end='')
    print('D' * m['D'])
    q -= 1
