def my_parse_int(stg):
    try:
        return int(stg)
    except ValueError:
        return "NaN"
