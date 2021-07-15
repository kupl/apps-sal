def is_palindrome(string):
    arr = []
    count = -1
    for i in str(string):
        arr.append(i)
    if arr[0] == arr[count]:
        count -= 1
        return True
    else:
        return False
