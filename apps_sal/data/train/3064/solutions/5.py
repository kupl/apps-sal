def transpose(arr):
    return [] if arr==[] else [[]] if arr[0]==[] else [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]
