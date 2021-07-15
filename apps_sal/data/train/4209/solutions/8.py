def largest_rect(histogram):
    lis, ris = [], []
    st = []
    for i in range(len(histogram)):
        while st and histogram[st[-1]] >= histogram[i]:
            st.pop()
        lis.append(st[-1] if st else -1)
        st.append(i)
    st = []
    for i in reversed(range(len(histogram))):
        while st and histogram[st[-1]] >= histogram[i]:
            st.pop()
        ris.append(st[-1] if st else len(histogram))
        st.append(i)
    return max((w * (ri - li - 1) for w, li, ri in zip(histogram, lis, reversed(ris))), default=0)
