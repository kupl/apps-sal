def rank_of_element(arr, i):
    return (
        sum(n <= arr[i] for n in arr[:i]) +
        sum(n <  arr[i] for n in arr[i + 1:]))
