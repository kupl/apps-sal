def odd(s):
    s = list(s)
    count = 0
    for k in range(len(s)):
        if s[k] == "o":
            for i in range(k+1, len(s)):
                if s[i] == "d":
                    for j in range(i+1, len(s)):
                        if s[j] == "d":
                            s[k] = "_"
                            s[i] = "_"
                            s[j] = "_"
                            count += 1
                            break
                    break
    return count

