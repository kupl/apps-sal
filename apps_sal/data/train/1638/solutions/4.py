def modi(s):
    return ''.join(['#'+i for i in s]) + '#'

def demodi(s):
    return ''.join(([i for i in s if i != '#']))

def longest_palindrome(s):
    s = modi(s)
    lenth, c, r, maxl, p = len(s), 0, 0, 0, [0]*len(s)

    for i in range(lenth):
        mir = (2*c) - i

        if i<r: 
            p[i] = min(r-i, p[mir])

        a, b = i + (1+p[i]), i - (1+p[i])
        while a < lenth and b >= 0 and s[a] == s[b]:
            p[i] += 1
            a += 1
            b -= 1

        if (i + p[i]) > r: 
            c = i
            r = i + p[i]

            if p[i] > maxl: 
                maxl = p[i]
    mai = p.index(maxl)
    return demodi(s[mai-maxl: mai+maxl+1])
