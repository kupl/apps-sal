def string_to_number(s):
    try:
        int(s)
        return int(s)
    except e:
        print("not an integer")
        pass
