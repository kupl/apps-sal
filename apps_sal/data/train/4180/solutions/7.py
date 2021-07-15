def lottery(s):
    result = set()
    result_seen = result.add
    result = [char for char in s if char.isdigit() and not (char in result or result_seen(char))]
    return "".join(result) if "".join(result).isnumeric() else "One more run!"
