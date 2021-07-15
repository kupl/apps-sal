def increment_string(strng):
    digit_count = 0
    for ch in strng[::-1]:
        if ch.isdigit():
            digit_count += 1
        else:
            break
    if not digit_count:
        return strng + '1'
    return f'{strng[: -digit_count]}{(int(strng[-digit_count:]) + 1):0{digit_count}}'

