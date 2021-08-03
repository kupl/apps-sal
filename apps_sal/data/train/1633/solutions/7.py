def to_chinese_numeral(n):
    return Chinese_Encoder(n).translated()


class Chinese_Encoder(object):
    def __init__(self, number):
        self.number = abs(number)
        self.sign = Sing(str(self.number), ('', "负")[number < 0], isinstance(number, float))
        self.get_num = lambda nums=self.sign.str: "".join(map(self._translate, nums))

    @property
    def get_tenth(self):
        return [self._translate(f"1{'0'* i}") for i in range(1, len(self.sign.str))][::-1]

    @staticmethod
    def _translate(n):
        return {0: "零", 1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七",
                8: "八", 9: "九", 10: "十", 100: "百", 1000: "千", 10000: "万"}.get(int(n))

    def _encod(self):
        if self.number < 20:
            return self._translate(self.sign.str) if self.number <= 10 else f'十{self.get_num()[-1]}'
        list_num, tenth, nums = [''], self.get_tenth, self.get_num()
        for i, n in enumerate(nums[:-1]):
            if n != '零':
                list_num.append(f'{n}{tenth[i]}')
            if n == '零' and list_num[-1] != n:
                list_num.append(n)
        return ''.join(list_num + [nums[-1]]).strip('零')

    def _encod_dec(self):
        return f'{ Chinese_Encoder(int(self.sign.str[:self.sign.dot_p])).translated() }{self.sign.dot}{self.get_num(self.sign.str[self.sign.dot_p+1:])}'

    def translated(self):
        method = (self._encod, self._encod_dec)[self.sign.is_float]
        return f'{self.sign.minus}{method()}'


class Sing:
    def __init__(self, find_d, minus, is_float):
        self.dot_p = find_d.find('.')
        self.minus = minus
        self.is_float = is_float
        self.dot, self.str = '点', find_d
