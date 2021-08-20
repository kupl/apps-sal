def capitalize(s):
    odd = s[::2]
    even = s[1::2]
    if len(odd) != len(even):
        even = even + ' '
    cap = ''
    for i in range(len(even)):
        cap += odd[i].upper() + even[i]
    cap2 = ''
    for i in range(len(even)):
        cap2 += odd[i] + even[i].upper()
    return [cap.strip(), cap2.strip()]
