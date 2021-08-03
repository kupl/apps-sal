def logical_calc(arr, op):

    answer = arr[0]

    if len(arr) >= 2:

        if op == "AND":
            for i in range(len(arr) - 1):
                answer &= arr[i + 1]

        if op == "OR":
            for i in range(len(arr) - 1):
                answer |= arr[i + 1]

        if op == "XOR":
            for i in range(len(arr) - 1):
                answer ^= arr[i + 1]

    return answer
