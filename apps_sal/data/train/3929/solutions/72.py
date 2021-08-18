def reverse(st):
    string = st.split()
    string.reverse()
    ans = ''
    for i in string:
        ans = ans + i + ' '
    return ans[:len(ans) - 1]
