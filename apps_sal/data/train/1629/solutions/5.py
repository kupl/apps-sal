def exchange_sort(s):
    t7, t8 = s.count(7), s.count(8)
    n97, n79 = s[:t7].count(9), s[t7 + t8:].count(7)
    n87, n98 = s[:t7].count(8), s[t7:t7 + t8].count(9)
    return 2 * n97 + n87 + n98 - min(n79, n97)    

