def switcher(arr):
    return ''.join(({'27': '!', '28': '?', '29': ' '}.get(e, chr(abs(int(e) - 26) + 97)) for e in arr))
