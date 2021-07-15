def pick_peaks(arr):
    ans = {"pos":[],"peaks":[]}
    for i in range(1,len(arr)-1):
        start = None
        end = None
        if arr[i-1] == arr[i]:
            for x in range(i,0,-1):
                while arr[i-x] != arr[i]:
                    start = i-x+1
                    break
        if arr[i+1] == arr[i]:
            for y in range(i,len(arr)-1):
                if arr[y] != arr[i]:
                    end = y -1
                    break
                else:
                    end = y
        if start == None: start = i
        if end == None: end = i
        if arr[start-1]< arr[start] and arr[end+1] < arr[end]:
            if start not in ans["pos"]:
                ans["pos"].append(start)
                ans["peaks"].append(arr[start])
    return ans
