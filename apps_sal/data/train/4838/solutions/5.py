def find_nth_occurrence(w, s, n=1, k=0):
    for i in range(len(s)):
        if s[i:i + len(w)] == w:
            k += 1
            if k == n:
                return i
    else:
        return -1
