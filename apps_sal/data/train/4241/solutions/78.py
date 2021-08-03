def sequence_sum(begin_number, end_number, step):
    x = []

    def lala(b, e, s):

        if b <= e:
            x.append(b)
            return lala(b + s, e, s)
        return x
    l = (lala(begin_number, end_number, step))
    print(l)
    return sum(l)
