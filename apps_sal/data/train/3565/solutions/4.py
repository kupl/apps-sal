import string
def solve(st,k): 
    for c in string.ascii_lowercase:
        count = st.count(c)
        st = st.replace(c,'',k)
        k -= count
        if k <= 0: break
    return st

