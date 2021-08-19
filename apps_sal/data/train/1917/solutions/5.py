class Solution:

    def __init__(self):
        self.i = 0
        self.formula = ''

    @staticmethod
    def _merge_into(dict_main, dict_added):
        """Change dict_main in place by adding the dict_added"""
        for (key, val) in list(dict_added.items()):
            dict_main[key] = dict_main.get(key, 0) + val

    @staticmethod
    def _multiply(dict_main, mult):
        """Return a new dict from the multiplication of everything by a number"""
        return {k: v * mult for (k, v) in list(dict_main.items())}

    def cur(self):
        return self.formula[self.i]

    def consume(self):
        res = self.formula[self.i]
        self.i += 1
        return res

    def atend(self):
        return self.i == len(self.formula)

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        self.formula = formula
        res = {}
        while not self.atend():
            self._merge_into(res, self.process_next_part())
        res_str = []
        for (key, value) in sorted(res.items()):
            res_str.append(key)
            if value != 1:
                res_str.append(str(value))
        return ''.join(res_str)

    def process_next_part(self):
        cur = self.cur()
        if cur.isalpha():
            name = self._consume_name()
            value = self._consume_digit()
            return {name: value}
        elif cur == '(':
            local_res = {}
            self.consume()
            while self.cur() != ')':
                self._merge_into(local_res, self.process_next_part())
            self.consume()
            value = self._consume_digit()
            return self._multiply(local_res, value)
        else:
            raise Exception('char unkwon')

    def _consume_name(self):
        name = self.consume()
        if not self.atend() and self.cur().isalpha() and (self.cur().lower() == self.cur()):
            return name + self.consume()
        return name

    def _consume_digit(self):
        if self.atend() or not self.cur().isdigit():
            return 1
        res_str = self.consume()
        while not self.atend() and self.cur().isdigit():
            res_str += self.consume()
        return int(res_str)
