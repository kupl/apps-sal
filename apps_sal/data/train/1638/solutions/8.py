def longest_palindrome(s):
    n = len(s)
    if n <= 1:
        return s
    (max, index) = (0, -1)
    (max2, index2) = (0, -1)
    d1 = [0] * n
    (i, l, r) = (0, 0, -1)
    while i < n:
        if i > r:
            k = 1
        else:
            k = min(d1[l + r - i], r - i + 1)
        while 0 <= i - k and i + k < n and (s[i - k] == s[i + k]):
            k += 1
        if k > max:
            (max, index) = (k, i)
        d1[i] = k
        k -= 1
        if i + k > r:
            (l, r) = (i - k, i + k)
        i += 1
    d2 = [0] * n
    (i, l, r) = (0, 0, -1)
    while i < n:
        if i > r:
            k = 0
        else:
            k = min(d2[l + r - i + 1], r - i + 1)
        while 0 <= i - k - 1 and i + k < n and (s[i - k - 1] == s[i + k]):
            k += 1
        if k > max2:
            (max2, index2) = (k, i)
        d2[i] = k
        k -= 1
        if i + k > r:
            (l, r) = (i - k - 1, i + k)
        i += 1
    index = index - max + 1
    max = 2 * max - 1
    index2 -= max2
    max2 *= 2
    (start, ln) = (0, 0)
    if max == max2:
        if index <= index2:
            (start, ln) = (index, max)
        else:
            (start, ln) = (index2, max2)
    elif max > max2:
        (start, ln) = (index, max)
    else:
        (start, ln) = (index2, max2)
    return s[start:start + ln]
