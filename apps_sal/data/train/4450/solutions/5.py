def consecutive(arr):
    if len(arr)<2 :
        return 0;
    arr.sort();
    return arr[-1]-arr[0]-len(arr)+1;
