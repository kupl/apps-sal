def cal_n_bug(n_head, n_leg, n_wing):
    spider = (n_leg-n_head*6)//(8-6)
    butterfly = (n_wing-(n_head-spider))
    dragonfly = n_head-spider-butterfly
    return [spider,butterfly,dragonfly] if spider>=0 and butterfly>=0 and dragonfly>=0 else [-1,-1,-1]
