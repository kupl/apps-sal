def tv_remote(words):
    kpad = ['abcde123fghij456klmno789pqrst.@0uvwxyz_/○ ☺☺☺☺☺', 'ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/○ ☺☺☺☺☺☺', '^~?!\'"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡☺☺☺_/○ ☺☺☺☺☺☺']
    (lenght, coord) = [0 for _ in range(2)]
    lst = list(kpad[0])
    for i in words:
        while kpad[0].find(i) == -1:
            (lenght, coord) = calculate(lst, '○', lenght, coord)
            kpad = kpad[-2:] + kpad[:-2]
            lst = list(kpad[0])
        (lenght, coord) = calculate(lst, i, lenght, coord)
    return lenght


def calculate(lst, i, lenght, coord):
    x = abs(lst.index(i) % 8 - coord % 8)
    y = abs(lst.index(i) // 8 - coord // 8)
    lenght += min(x, 8 - x) + min(y, 6 - y) + 1
    return [lenght, lst.index(i)]
