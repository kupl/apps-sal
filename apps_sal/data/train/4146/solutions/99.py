def is_sorted_and_how(arr):
    # your code here
    s = "no"
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            s = "yes"
            z = "ascending"
        else:
            s = "no"
            z = ""
            break
    if s == "no":

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                s = "yes"
                z = "descending"
            else:
                s = "no"
                z = ""
                break
    if s == "no":
        return s
    else:
        return (s + ", " + z)
