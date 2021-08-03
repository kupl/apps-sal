def head_smash(arr):
    if arr == [] or arr == "":
        return "Gym is empty"
    if isinstance(arr, int):
        return "This isn't the gym!!"
    res = []
    for i in arr:
        res.append(i.replace("O", " "))
    return res
