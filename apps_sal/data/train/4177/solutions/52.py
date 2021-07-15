def men_from_boys(arr):
    return [i for i in sorted(list(set(arr))) if i%2==0]+[i for i in sorted(list(set(arr)))[::-1] if i%2==1]
