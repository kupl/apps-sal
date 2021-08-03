def obtain_max_number(arr):
    while sorted(arr) != sorted(list(set(arr))):
        new_arr = []
        checked = []
        for i in arr:
            if arr.count(i) >= 2 and i not in checked:
                checked.append(i)
                n = [i * 2] * (arr.count(i) // 2) if arr.count(i) % 2 == 0 else [i * 2] * (((arr.count(i) - 1)) // 2) + [i]
                new_arr.extend(n)
            elif arr.count(i) < 2 and i not in checked:
                checked.append(i)
                new_arr.append(i)

        arr = new_arr[:]

    return max(arr)
