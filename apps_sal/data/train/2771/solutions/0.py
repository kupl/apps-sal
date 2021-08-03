def hofstadter_Q(n):
    try:
        return hofstadter_Q.seq[n]
    except IndexError:
        ans = hofstadter_Q(n - hofstadter_Q(n - 1)) + hofstadter_Q(n - hofstadter_Q(n - 2))
        hofstadter_Q.seq.append(ans)
        return ans


hofstadter_Q.seq = [None, 1, 1]
