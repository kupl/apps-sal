def fst2_lst2(arr):
    return chr(arr[0])+chr(arr[1])+chr(arr[-2])+chr(arr[-1])
    
def sort_transform(arr):
    asc_arr = sorted([chr(n) for n in arr])
    return fst2_lst2(arr) + '-' + fst2_lst2(sorted(arr)) + '-' + fst2_lst2(sorted(arr, reverse=True)) + '-' + asc_arr[0]+asc_arr[1]+asc_arr[-2]+asc_arr[-1]
