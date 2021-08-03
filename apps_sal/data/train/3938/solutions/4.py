def sorted_brands(history):
    count = {}
    for i in history:
        count[i['brand']] = count.get(i['brand'], 0) + 1
    return sorted(count, key=lambda x: -count[x])
