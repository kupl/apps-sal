def pseudo_sort(st):
    words = st.translate(str.maketrans("", "", ".,:;!?")).split()
    lower, upper = [], []

    for word in words:
        if word[0].isupper():
            upper.append(word)
        else:
            lower.append(word)

    return " ".join(sorted(lower) + sorted(upper, reverse=True))
