def get_honor_path(h, t):
    return {k + 'kyus': v for k, v in zip("12", divmod(t - h, 2))} if t > h else {}
