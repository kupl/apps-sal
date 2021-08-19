def find_middle(string):
    # Если в String подаётся None, возвращаем -1
    if string is None:
        return -1
    # Если в String подаётся число, возвращаем -1
    if type(string) is int:
        return -1

    # Если в String передаётся массив, возвращаем -1
    if type(string) is list:
        return -1

    # Создаём массив и вносим туда только числа из String
    spisok = []
    for i in string:
        if i.isdigit():
            spisok.append(i)

    # Если в String не было чисел, значит возвращаем -1
    if len(spisok) == 0:
        return -1

    # Создаём переменную, в которой будет хранится число после перемножения всех чисел
    spisok_ans = 1

    # Перемножаем все числа
    for i in spisok:
        spisok_ans *= int(i)

    # Переводим итоговое число в текст, для соблюдения условия задачи
    spisok = str(spisok_ans)

    # Если спи
    if len(spisok) % 2 == 0:
        if len(spisok) >= 2:
            spisok[:1].replace("0", "")
        test = int(len(spisok) / 2)
        answer = spisok[test - 1:test + 1]
    else:
        test = int(len(spisok) / 2)
        answer = spisok[test:test + 1]

    answer = "".join(answer)
    return int(answer)
