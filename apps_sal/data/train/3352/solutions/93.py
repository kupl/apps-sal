def find_longest(arr):
    digit_lengths = list(map(lambda x: len(str(x)), arr))
    return arr[
        digit_lengths.index(max(digit_lengths))
    ]
