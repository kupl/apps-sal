def reverse(st):
    res = ''
    arr = st.split()
    for k in reversed(arr):
        res += f'{k} '
    return res[:-1]
