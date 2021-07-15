def solve(arr):
    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    arr2 = []
    for el in arr:
        count = 0
        for i in range(len(el)):
            if el.lower()[i] == abc[i]:
                count = count + 1
        arr2.append(count)
    return arr2       
