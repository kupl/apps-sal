def available_moves(position):
    result = []
    try:
        letter = position[0]
        number = int(position[1:])
        if number < 1 or number > 8:
            return result
        if ord(letter) < 65 or ord(letter) > 72:
            return result
        for i in range(65, 73):
            for j in range(1, 9):
                if chr(i) == letter:
                    result.append(letter + str(j))
                elif j == number:
                    result.append(chr(i) + str(number))
                elif abs(j - number) == abs(i - ord(letter)):
                    result.append(chr(i) + str(j))
        result.remove(position)
    except Exception:
        pass
    return result
