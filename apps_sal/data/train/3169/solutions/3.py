def count_odd_pentaFib(n):
    st = [0, 1]
    count = 0
    if 0< n < 2: return 1
    if n <= 0 : return 0
    while n >= 2:
        if sum(st[-5:]) % 2 != 0: count += 1
        st.append(sum(st[-5:]))
        n -= 1
    return count
