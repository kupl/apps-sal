def rotate(arr, n):
    rot = -n % len(arr)
    return arr[rot:] + arr[:rot]
