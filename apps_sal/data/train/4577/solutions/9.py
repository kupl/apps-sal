def debug(s):
    result = s.replace("bugs", "&")
    result = result.replace("bug", "")
    result = result.replace("&", "bugs")
    return result
