def merge(line):
    viper = [x for x in line if x]
    if len(viper) > 1:
        head, neck = viper[:2]
        equal = head == neck
        head += neck * equal
        tail = merge(viper[1 + equal:])
        return [head] + tail + [0] * (len(line) - len(tail) - 1)
    else:
        return line
