def swap(word):
    m = len(word) // 2
    if len(word) % 2 == 0:
        return word[:m][::-1] + word[m:][::-1]
    else:
        return word[:m][::-1] + word[m] + word[m + 1:][::-1]


def inside_out(st):
    return ' '.join(map(swap, st.split()))
