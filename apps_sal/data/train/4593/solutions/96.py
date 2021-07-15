def merge_arrays(arr1, arr2):
    merged = []
    for number in arr1 + arr2:
        if number not in merged:
            merged.append(number)
    return sorted(merged)
