def tiy_fizz_buzz(s):
    uv = [chr(x) for x in [65,69,73,79,85]]
    lv = [chr(x) for x in [97,101,105,111,117]]
    u = [chr(x) for x in range(66,91)]
    return ''.join(["Iron Yard" if x in uv else "Iron" if x in u else "Yard" if x in lv else x for x in list(s)])
