def solve(s):
    max = 0
    
    for i in range(len(s)):
        if s[i].isnumeric():
            k = ""
            for j in range(i, len(s)):
                if s[j].isnumeric():
                    k+=s[j]
                    if max < int(k):
                        max = int(k)
                else:
                    if max < int(k):
                        max = int(k)
                    break
    return max    
