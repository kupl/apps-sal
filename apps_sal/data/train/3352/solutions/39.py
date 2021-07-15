def find_longest(arr):
    a=sorted(arr,key=lambda x: len(str(x)))
    for i in a:
        if len(str(i))==len(str(a[-1])):
            return i
