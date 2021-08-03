def transpose(amount, tab):
    position = []
    position_neg = False
    result = []
    for line in tab:
        res = ''
        for counter, letter in enumerate(line):
            if letter.isdigit():
                if line[counter - 1].isdigit():
                    continue
                if line[counter + 1].isdigit():
                    if (int(letter + line[counter + 1]) + amount) <= 22:
                        res += str(int(letter + line[counter + 1]) + amount)
                        if len(str(int(letter + line[counter + 1]) + amount)) == 1:
                            position.append(counter)
                            position_neg = True
                    else:
                        return 'Out of frets!'
                else:
                    if len(str(int(letter) + amount)) == 2:
                        if int(letter) + amount < 0:
                            return 'Out of frets!'
                        res += str(int(letter) + amount)
                        position.append(counter)
                    else:
                        res += str(int(letter) + amount)
            else:
                res += letter
        result.append(res)

    position = list(set(position))
    position.sort()
    for counter, line in enumerate(result):
        added = 0
        for insert in position:
            if not position_neg:
                double_in_col = False
                for line2 in tab:
                    if line2[insert].isdigit() and line2[insert + 1].isdigit():
                        double_in_col = True
                if double_in_col:
                    if result[counter][insert + added].isdigit():
                        if result[counter][insert + added + 1].isdigit():
                            if not tab[counter][insert + 1].isdigit():
                                result[counter] = result[counter][:insert + added + 2] + result[counter][insert + added + 3:]
                else:
                    if result[counter][insert + added].isdigit():
                        if result[counter][insert + added + 1].isdigit():
                            if tab[counter][insert + 1].isdigit():
                                result[counter] = result[counter][:insert + added + 2] + '-' + result[counter][insert + added + 2:]
                        else:
                            result[counter] = result[counter][:insert + added + 1] + '-' + result[counter][insert + added + 1:]
                    else:
                        result[counter] = result[counter][:insert + added + 1] + '-' + result[counter][insert + added + 1:]
                    added += 1
            else:
                double_in_col = False
                for line2 in result:
                    if line2[insert + added].isdigit() and line2[insert + 1 + added].isdigit():
                        double_in_col = True
                if double_in_col:
                    if result[counter][insert + added].isdigit():
                        if not result[counter][insert + added + 1].isdigit():
                            if tab[counter][insert + 1].isdigit():
                                result[counter] = result[counter][:insert + added + 1] + '-' + result[counter][insert + added + 1:]
                else:
                    if result[counter][insert + added].isdigit():
                        if not result[counter][insert + added + 1].isdigit():
                            if tab[counter][insert + 1].isdigit():
                                added -= 1
                                continue
                    result[counter] = result[counter][:insert + added + 2] + result[counter][insert + added + 3:]
                    added -= 1
    return result
