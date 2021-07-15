def cal_n_bug(heads, legs, wings):
    spiders = legs // 2 - heads * 3
    dragonflies = wings + spiders - heads
    r = [spiders, heads - spiders - dragonflies, dragonflies]
    return r if all(x >= 0 for x in r) else [-1] * 3
