def reverse(st):
    n = ""
    s = st.split()
    i = len(s) - 1
    while i >= 0:
        if i == len(s) - 1:
            n = n + s[i]
            i = i - 1
            continue
        n = n + " " + s[i]
        i = i - 1
    return n
