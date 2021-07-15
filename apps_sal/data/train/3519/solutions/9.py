def duplicate_elements(m, n):
    for element in m:
        try:
            n.index(element)
            return True
        except:
            continue
    return False
