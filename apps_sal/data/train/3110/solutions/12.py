def two_decimal_places(n):
    pot_location = 0
    lt = list(str(n))
    for i in range(0, len(lt)):
        if lt[i] == '.':
            pot_location = i
            break
    result = float(''.join(lt[:pot_location + 3]))
    if int(lt[pot_location + 3]) > 4:
        if n > 0:
            result = result + 0.01
        else:
            result = result - 0.01
    return round(result, 5)
