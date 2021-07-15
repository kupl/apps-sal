def encode(s):
    try:
        arr = [s]
        for i in range(1, len(s)):
            arr.append(s[-i:] + s[:-i])
        arr.sort()
        res_str = ''
        for el in arr:
            res_str += el[-1]
        return (res_str, arr.index(s))
    except:
        return (s, len(s))
    

def decode(s, n):
    try:
        m = [''] * (len(s))
        for i in range(len(s)):
            for j in range(len(s)):
                m[j] = s[j] + m[j]
            m.sort()
        return m[n]
    except:
        return ''

