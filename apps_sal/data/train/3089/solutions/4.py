def dashatize(num):
    array = []

    # Вызываем Исключение.
    if num == None:
        return "None"
    elif num == 0:
        return "0"
    elif num == -1:
        return "1"

    # Если, входное число отрицательное - убрать минус.
    num = str(num).replace('-', '')
    
    # Перебор элементов и проверка его на [Чётность] и [Нечётность].
    for i in str(num):
        if int(i) % 2 == 0:
            array.append(i)
        else:
            array.append('-'+ i +'-')

    # Соединяем в строку.
    string = ''.join(array)

    # Фильтруем.
    if string[0] == '-' and string[-1] == '-':
        string = string[1:-1]
    if string[0] == '-':
        string = string[1:]
    if string[-1] == '-':
        string = string[:-1]
    result = string.replace('--', '-')

    # Возвращаем [result].
    return result
