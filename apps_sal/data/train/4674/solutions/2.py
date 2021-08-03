DELTA = ord("a") - 1


def sumName(name):
    return sum(ord(c) - DELTA for c in name) + len(name)


def rank(st, we, n):
    return ("No participants" if st == "" else
            "Not enough participants" if n > st.count(",") + 1 else
            sorted((-sumName(name.lower()) * w, name) for name, w in zip(st.split(','), we))[n - 1][1])
