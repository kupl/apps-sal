def increment_string(strng):
    head = strng.rstrip('1234567890')
    tail = strng[len(head):]
    return head + str(int('0' + tail) + 1).zfill(len(tail))
