def length_of_sequence(arr, n):
    try:
        i = arr.index(n)
        j = arr.index(n, i + 1)
        try:
            arr.index(n, j + 1)
            return 0
        except ValueError:
            return j - i + 1
    except ValueError:
        return 0
