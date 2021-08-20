def binary_array_to_number(arr):
    binary = ''.join(map(str, arr))
    ans = 0
    for i in range(len(binary)):
        ans += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return ans
