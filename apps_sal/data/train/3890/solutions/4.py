def get_honor_path(hs, ths):
    return {'2kyus': (ths - hs) % 2, '1kyus': int((ths - hs) / 2)} if ths > hs else {}
