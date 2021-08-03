def total(arr):
    sum = 0
    erastoteme = [True] * len(arr)
    for num in range(2, len(erastoteme)):
        if erastoteme[num]:
            sum += arr[num]
            for nb in range(num * 2, len(erastoteme), num):
                erastoteme[nb] = False
    return sum
