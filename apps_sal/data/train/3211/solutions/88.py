def divide(m):
    if m == 2:
        return False
    return (m-2)%2 == 0 and (m-(m-2))%2 == 0
