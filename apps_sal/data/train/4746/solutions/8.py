def fisHex(name):
    print(name)
    hex_string = 'abcdef'
    name = name.lower()
    values = [i for i in name if i in hex_string]
    if len(values) >= 1:
        placeholder = int(str(values.pop()), 16)
        for num in values:
            placeholder = placeholder ^ int(num, 16)
        return placeholder
    else:
        return 0
