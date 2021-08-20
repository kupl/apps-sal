def majority(arr):
    cnt = sorted(([arr.count(i), i] for i in set(arr)), reverse=True)
    if len(cnt) == 1 or (len(cnt) > 1 and cnt[0][0] != cnt[1][0]):
        return cnt[0][1]
    else:
        return None
