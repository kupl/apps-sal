def sequence_classifier(arr):
    strict, increasing, decreasing = True, False, False

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            strict = False
        if arr[i] < arr[i - 1]:
            decreasing = True
        if arr[i] > arr[i - 1]:
            increasing = True

    return [increasing and decreasing,  # unordered
            strict and increasing,  # strictly increasing
            not strict and increasing,  # not decreasing
            strict and decreasing,  # strictly decreasing
            not strict and decreasing,  # not increasing
            not increasing and not decreasing].index(True)  # constant
