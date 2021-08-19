def locate(arr, item):
    return item in arr or any((isinstance(e, (list, tuple)) and locate(e, item) for e in arr))
