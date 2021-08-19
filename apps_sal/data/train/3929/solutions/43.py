def reverse(st):
    ls = st.split()
    result = []
    for i in range(len(ls) - 1, -1, -1):
        result.append(ls[i])
    result = ' '.join(result)
    return result
