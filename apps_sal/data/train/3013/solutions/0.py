def delete_digit(n):
    s = str(n)
    return int(max(s[:i] + s[i+1:] for i in range(len(s))))
