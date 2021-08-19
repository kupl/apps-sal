def tribonacci(s, n):
    if(n > 3):
        for i in range(n - 3):
            s.append(s[i] + s[i + 1] + s[i + 2])
        return s
    else:
        return s[:n]
    # your code here
