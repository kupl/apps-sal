def first_non_consecutive(arr):
    # your code here
    a = [arr[i + 1] for i in range(len(arr)) if i + 1 < len(arr) and arr[i + 1] - arr[i] > 1]
    print(a)
    return a[0] if len(a) > 0 else None
