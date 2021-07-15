class Simplexer:
    def __init__(self, expression):
        self.n = 0
        self.keywords = ['if', 'else', 'for', 'while', 'return', 'func', 'break']
        self.whitespace_chars = [' ', '\t', '\r', '\n', '\v', '\f']
        self.expression = expression
        self.work_dict = {}
        self.__build()
        self.tokens = [
            Token(text=self.work_dict[x]['text'], type=self.work_dict[x]['type'])
            for x in sorted(self.work_dict.keys(), key=lambda x: int(x.split(',')[0]))
        ]

    def __iter__(self):
        for x in self.tokens:
            yield x

    def __next__(self):
        if len(self.tokens) == 0:
            raise StopIteration
        if self.n < len(self.tokens):
            self.n += 1
            return self.tokens[self.n - 1]
        else:
            raise StopIteration

    def __str__(self):
        return ', '.join([str(t) for t in self.tokens])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Simplexer):
            if len(self) != len(other):
                return False
            for t in self.tokens:
                found = False
                for t2 in other.tokens:
                    if t.text == t2.text and t.type == t2.type:
                        found = True
                        break
                if not found:
                    return False
            return True
        elif isinstance(other, list):
            for t in self.tokens:
                found = False
                for t2 in other:
                    if t.text == t2.text and t.type == t2.type:
                        found = True
                        break
                if not found:
                    return False
            return True
        else:
            return False

    def __build(self):
        self.__handle_integers()
        self.__handle_booleans()
        self.__handle_strings()
        self.__handle_operators()
        self.__handle_keywords()
        self.__handle_whitespaces()
        self.__handle_identifiers()

    def __handle_integers(self):
        i = 0
        count = 0
        while i < len(self.expression) and count < len(self.expression):
            if self.expression[i].isdigit():
                c = self.expression[i]
                numbers = [c]
                count = i + 1
                while c.isdigit() and count < len(self.expression):
                    c = self.expression[count]
                    if not c.isdigit():
                        break
                    numbers.append(c)
                    count += 1
                self.work_dict[f"{i},{count}"] = {
                    'text': ''.join(numbers),
                    'type': 'integer'
                }
            else:
                count += 1
            i = count

    def __handle_booleans(self):
        import re
        true_idxes = [f"{m.start()},{m.end()}" for m in re.finditer('true', self.expression)]
        for t in true_idxes:
            self.work_dict[t] = {
                'text': 'true',
                'type': 'boolean'
            }
        false_idxes = [f"{m.start()},{m.end()}" for m in re.finditer('false', self.expression)]
        for t in false_idxes:
            self.work_dict[t] = {
                'text': 'false',
                'type': 'boolean'
            }

    def __handle_strings(self):
        import re
        pattern = r'".*?"'
        idxes = [f'{m.start()},{m.end()}' for m in re.finditer(pattern, self.expression)]
        for t in idxes:
            start, end = [int(elem) for elem in t.split(',')]
            self.work_dict[t] = {
                'text': self.expression[start: end],
                'type': 'string'
            }

    def __handle_operators(self):
        for i in range(len(self.expression)):
            if self.expression[i] in ['+', '-', '*', '/', '%', '(', ')', '=']:
                self.work_dict[f"{i},{i + 1}"] = {
                    'text': self.expression[i],
                    'type': 'operator'
                }

    def __handle_keywords(self):
        import re
        for word in self.keywords:
            idxes = [f'{m.start()},{m.end()}' for m in re.finditer(word, self.expression)]
            for t in idxes:
                start, end = [int(elem) for elem in t.split(',')]
                self.work_dict[t] = {
                    'text': self.expression[start: end],
                    'type': 'keyword'
                }
        return

    def __handle_whitespaces(self):
        i = 0
        count = 0
        while i < len(self.expression) and count < len(self.expression):
            if self.expression[i] in self.whitespace_chars:
                c = self.expression[i]
                spaces = [c]
                count = i + 1
                while c in self.whitespace_chars and count < len(self.expression):
                    c = self.expression[count]
                    if c not in self.whitespace_chars:
                        break
                    spaces.append(c)
                    count += 1
                self.work_dict[f"{i},{count}"] = {
                    'text': ''.join(spaces),
                    'type': 'whitespace'
                }
            else:
                count += 1
            i = count

    def __handle_identifiers(self):
        sorted_keys = sorted(self.work_dict.keys(), key=lambda x: int(x.split(',')[0]))
        if len(sorted_keys) == 0:
            if len(self.expression) == 1:
                self.work_dict['0,1'] = {
                    'text': self.expression,
                    'type': 'identifier'
                }
            return
        start = int(sorted_keys[0].split(',')[0])
        if start != 0:
            self.work_dict[f'0,{start}'] = {
                'text': self.expression[0: start],
                'type': 'identifier'
            }

        end = int(sorted_keys[-1].split(',')[1])
        if end != len(self.expression):
            self.work_dict[f'{end},{len(self.expression)}'] = {
                'text': self.expression[end: len(self.expression)],
                'type': 'identifier'
            }
        prev_end = int(sorted_keys[0].split(',')[1])
        for key in sorted_keys:
            start, end = [int(x) for x in key.split(',')]
            if start != prev_end and self.expression[prev_end: start] != "":
                self.work_dict[f'{prev_end},{start}'] = {
                    'text': self.expression[prev_end: start],
                    'type': 'identifier'
                }
            prev_end = end


class Token:

    def __init__(self, text, type):
        self.text = text
        self.type = type

    def __str__(self):
        return f'Token("{self.text}", "{self.type}")'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.text == other.text and self.type == other.type
        return False
