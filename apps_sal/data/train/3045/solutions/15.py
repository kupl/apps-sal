def elevator(left, right, call):
    return ('right', 'left')[right < left <= call or call <= left < right]
