def next_item(xs, item):
    idx = None
    cnt = 0
    for (i, e) in enumerate(xs):
        if cnt == 1:
            break
        if e == item:
            idx = i
            cnt += 1
    print(xs)
    print(e, i, idx)
    if idx == i:
        return None
    try:
        print('first')
        print(xs[idx])
        return xs[i]
    except:
        if idx is None:
            print('second')
            return idx
        print('third')
        return e
