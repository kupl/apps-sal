def next_version(version):
    print(version)
    array_version = version.split('.')
    last_index = len(array_version) - 1
    start = 0
    add_value = 1
    while last_index >= 0:
        value_last_part_version = int(array_version[last_index]) + add_value
        if '0' in str(value_last_part_version):
            if last_index != 0:
                array_version[last_index] = str(0)
            else:
                array_version[last_index] = str(value_last_part_version)
            if len(str(value_last_part_version)) != 1:
                add_value = 1
            else:
                add_value = 0
        else:
            add_value = 0
            array_version[last_index] = str(value_last_part_version)
        last_index -= 1
    return '.'.join(array_version)
