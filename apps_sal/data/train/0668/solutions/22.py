for i in range(int(input())):
    n, k = (map(int, input().split()))
    l = list(map(int, input().split()))
    if k == 1:
        c_sum = l[0]
        m_sum = l[0]
        for i in range(1, n):
            c_sum = max(l[i], c_sum + l[i])
            m_sum = max(m_sum, c_sum)
        print(m_sum)
    else:
        s = sum(l)
        l *= 2
        j = 1
        c_sum = l[0]
        m_sum = l[0]
        while j < 2 * n:
            if l[j] > c_sum + l[j]:
                c_sum = l[j]
            else:
                c_sum += l[j]
            if c_sum > m_sum:
                m_sum = c_sum
            j += 1
        if s <= 0:
            print(m_sum)
        else:
            print(m_sum + (k - 2) * s)
