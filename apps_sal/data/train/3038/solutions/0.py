def solve(st):
    return sorted((st.find(c) - st.rfind(c), c) for c in set(st))[0][1]
