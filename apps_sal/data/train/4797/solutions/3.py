def shorter_reverse_longer(a,b):
    short,long = sorted((b,a), key=len)
    return short + long[::-1] + short
