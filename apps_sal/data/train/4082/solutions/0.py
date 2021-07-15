def sequence_classifier(arr):
    if all(arr[i] == arr[i+1] for i in range(len(arr)-1)): return 5
    if all(arr[i] <  arr[i+1] for i in range(len(arr)-1)): return 1
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)): return 2
    if all(arr[i] >  arr[i+1] for i in range(len(arr)-1)): return 3
    if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)): return 4
    return 0
