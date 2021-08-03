def jumping_number(n):
    s = str(n)
    return "Jumping!!" if all(s[i:i + 2] in "0123456789876543210" for i in range(len(s))) else "Not!!"
