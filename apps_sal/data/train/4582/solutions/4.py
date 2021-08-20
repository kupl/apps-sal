def group(arr):
    (st, res) = (set(arr), [])
    for n in arr:
        if n in st:
            st.remove(n)
            res.append([n] * arr.count(n))
    return res
