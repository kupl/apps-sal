def tail_swap(s):
    h1,t1 = s[0].split(':')
    h2,t2 = s[1].split(':')
    return ['{}:{}'.format(h1,t2), '{}:{}'.format(h2,t1)]
