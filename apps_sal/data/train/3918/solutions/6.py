def baby_count(x):
    T = [x.lower().count(e) // (2 if e == 'b' else 1)for e in 'bay']
    print(T)
    return min(T) if min(T) != 0 else 'Where\'s the baby?!'
