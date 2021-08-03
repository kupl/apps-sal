def men_from_boys(arr):
    odd = []
    even = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1 and arr[i] not in odd:
            odd.append(arr[i])
        elif arr[i] % 2 == 0 and arr[i] not in even:
            even.append(arr[i])
    final_odd = sorted(odd, reverse=True)
    final_even = sorted(even)
    output = final_even + final_odd
    return output
    # separate arr in even and odd
    # then combine even and odd numbers
