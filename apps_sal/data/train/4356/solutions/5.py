def colorful(number):
    if len(str(number)) == 1:
        return True
    else:
        output = list(str(number))
        for n, x in enumerate(list(str(number))):
            if n + 1 < len(str(number)):
                tmp = list(str(number))[n + 1]

                output.append(str(int(x) * int(tmp)))

        if len(output) == len(set(output)):
            return True
        else:
            return False
