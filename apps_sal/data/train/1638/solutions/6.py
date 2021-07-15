def longest_palindrome(s):
    s = "_" + '_'.join(s) + "_"
    n = len(s)
    a = [0] * n

    rb = ml = mctr = ctr = c = 0

    for i in range(1,n):
        a[i] = min(rb-i, a[2*ctr-i]) if rb > i else 1
        c = a[i]
        while i+c < n and i >= c and s[i-c] == s[i+c]: c += 1
        a[i] = c
        if i+c > rb:
            rb = i+c
            ctr = i
        if c > ml:
            ml = c
            mctr = i

    return s[mctr-ml+1 : mctr+ml].replace('_', "")
