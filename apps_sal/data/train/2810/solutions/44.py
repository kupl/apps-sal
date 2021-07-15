def solve(arr):
    result = []
    counter_correct = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for a in arr:
        a = a.lower()
        counter_correct = 0
        for i in range(len(a)):
            if i == alphabet.index(a[i]):
                counter_correct += 1
        result.append(counter_correct)
    return result
