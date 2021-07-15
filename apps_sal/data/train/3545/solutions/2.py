def well(arr):
    nb_good = sum(1 for lst in arr for word in lst if str(word).lower() == "good")
    return "I smell a series!" if nb_good > 2 else "Publish!" if nb_good > 0 else "Fail!"

