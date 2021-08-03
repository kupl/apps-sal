def longer(strng):
    def length_string(s):
        return len(s)
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=length_string))
    return result
