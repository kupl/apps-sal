def inside_out(st):
    def inside_out_1(st):
        h, m = divmod(len(st), 2)
        return st[:h][::-1] + st[h:h + m] + st[h + m:][::-1]
    return ' '.join(map(inside_out_1, st.split(' ')))
