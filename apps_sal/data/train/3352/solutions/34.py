def find_longest(arr):
    box=[]
    position=0
    base=0
    for i,e in enumerate(arr):
        for j in str(e):
            box.append(j)
        if len(box)>base:
            base=len(box)
            result=i
        box.clear()
    return arr[result]

