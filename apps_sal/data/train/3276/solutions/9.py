def missing(nums, str):
    try:
        return ''.join(str.replace(' ','')[i].lower() for i in sorted(nums))
    except:
        return "No mission today"
