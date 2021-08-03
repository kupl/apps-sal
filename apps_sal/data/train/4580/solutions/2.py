def tiaosheng(fails):
    return 60 - sum(1 for i, f in enumerate(fails) for k in range(3) if 3 * i + f + k < 60)
