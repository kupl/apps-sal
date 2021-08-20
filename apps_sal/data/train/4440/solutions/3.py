def merge(array1, array2):
    array3 = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i = i + 1
        else:
            array3.append(array2[j])
            j = j + 1
    return array3 + array1[i:] + array2[j:]


def validate_pin(pin):
    key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(pin) == 6 or len(pin) == 4:
        p = [i for i in pin]
        m = merge(key, p)
        if len(set(m)) == len(key):
            return True
        return False
    else:
        return False
