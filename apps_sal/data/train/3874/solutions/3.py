def sort_twisted37(arr):
    return list(sorted(arr, key=lambda x: int(str(x).translate("".maketrans("37", "73")))))
