def pick_peaks(arr):
    ans = {"peaks" :[] ,"pos": []}
    point = False
    for i in range(len(arr)):
        if arr[i]> arr[i-1]:
            point = i
        elif arr[i] < arr[i-1] and point:
            ans["pos"].append(point)
            ans["peaks"].append(arr[point])
            point = False
    return ans
    #your code here

