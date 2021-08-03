def clean_mean(arr, cutoff):
    while True:
        mean, prev = sum(arr) / len(arr), arr
        S_D = (sum((i - mean) ** 2 for i in arr) / len(arr)) ** .5
        actual = S_D * cutoff
        arr = [i for i in arr if abs(i - mean) < actual]
        if prev == arr:
            return round(sum(arr) / len(arr), 2)
