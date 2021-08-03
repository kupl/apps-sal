def count_smileys(arr):
    return len(list(filter(lambda x: x in [':D', ':~D', ':-D', ';D', ';~D', ';-D', ':)', ':~)', ':-)', ';)', ';~)', ';-)'], arr)))
