def well(arr):
    total = 0
    for i in arr:
        for j in i:
            if isinstance(j, str) and j.lower() == 'good':
                total += 1
    return 'Fail!' if total == 0 else 'I smell a series!' if total > 2 else 'Publish!'

