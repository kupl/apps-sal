def is_bouncy(number):
    return sorted(str(number)) != list(str(number)) != sorted(str(number))[::-1]
