def increment_string(strng):
    nums = "0123456789"
    num = ""
    digits = 0
    for char in reversed(strng):
        if char in nums:
            num = char + num
            digits += 1
        else: break
    return strng.rstrip(num) + str(int(num)+1).zfill(digits) if len(num) >0 else strng + "1"
