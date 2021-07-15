def missing(nums, str):
    str=str.replace(' ','').lower()
    try:
        return ''.join(str[i] for i in sorted(nums))
    except:
        return "No mission today"
