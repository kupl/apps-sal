def next_item(seq, item):

    if type(seq) in [list, str]:
        return seq[seq.index(item) + 1] if ((item != seq[-1]) + (item in seq)) == 2 else None

    else:
        bar = next(seq)
        foo = next(seq)
        foobar = item + (foo - bar)

        last_item = 0
        for i in range(700):
            try:
                c = seq.__next__()
                if c is not None:
                    last_item = c
            except StopIteration:
                break

        return foobar if foobar < last_item else None
