def count_smileys(arr):
    count = 0
    if not arr:
        return 0
    smileys = [':)', ';)', ':~)', ';~)', ':-)', ';-)', ':D', ';D', ':~D', ';~D', ':-D', ';-D']
    for i in arr:
        if i in smileys:
            count += 1
    return count
