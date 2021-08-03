def increment_string(strng):
    if strng.isdigit():
        return '0' * (len(strng) - len(str(int(strng) + 1))) + str(int(strng) + 1)
    numbers = ''
    for i in range(len(strng[-1::-1])):
        if i == 0 and not strng[-1::-1][i].isdigit():
            break
        if strng[-1::-1][i].isdigit():
            numbers += strng[-1::-1][i]
        else:
            strng = strng[: -i]
            numbers = numbers[-1::-1]
            break
    lenght = len(numbers)
    numbers = int(numbers) + 1 if numbers else 1
    return strng + '0' * (lenght - len(str(numbers))) + str(numbers)
