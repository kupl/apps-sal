def sort_transform(arr):
    a=chr(arr[0])+chr(arr[1])+chr(arr[-2])+chr(arr[-1])
    arr.sort()
    b=chr(arr[0])+chr(arr[1])+chr(arr[-2])+chr(arr[-1])
    return '-'.join([a,b,b[::-1],b])
