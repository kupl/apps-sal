def char_freq(message):
    cnt = dict()
    for ch in list(message):
        print('ch : ', ch)
        if ch in cnt:
            cnt[ch] += 1
        else:
            cnt[ch] = 1
    return cnt
