def increment_string(strng):
    text = strng.rstrip('0123456789')
    nums = strng[len(text):]
    if nums == "": return strng+"1"
    return text + str(int(nums) + 1).zfill(len(nums))
