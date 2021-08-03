def repeat_str(src, count):
    try:
        if src == int(src):
            return (src * count)
    except ValueError:
        return 'Error'
