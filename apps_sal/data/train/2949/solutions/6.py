def split_and_add(numbers, n):

    def splitter(arr):
        (left, right) = (([0] if len(arr) % 2 != 0 else []) + arr[:len(arr) // 2], arr[len(arr) // 2:])
        return [l + r for (l, r) in zip(left, right)]
    return numbers if n == 0 else split_and_add(splitter(numbers), n - 1)
