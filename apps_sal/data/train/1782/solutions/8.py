TOKENS_TYPE = {'+': 'operator', '-': 'operator', '*': 'operator', '/': 'operator', '%': 'operator', '(': 'operator', ')': 'operator', '=': 'operator', 'true': 'boolean', 'false': 'boolean', 'if': 'keyword', 'for': 'keyword', 'while': 'keyword', 'else': 'keyword', 'return': 'keyword', 'func': 'keyword', 'break': 'keyword', ' ': 'whitespace'}


class Token:

    def __init__(self, text: str, type: str):
        self.text = text
        self.type = type

    def __eq__(self, other):
        return self.text == other.text and self.type == other.type

    def __repr__(self):
        return f"<'{self.text}': {self.type}>"


class Simplexer:

    def __init__(self, expression):
        self.exp = expression
        self.num = 0
        self.parsed_exp = self._parse()

    @staticmethod
    def _get_split_chars(char_types: list):
        split_types = []
        temp_type = (0, char_types[0][-1])
        for i in range(len(char_types)):
            if char_types[i][-1] != temp_type[-1]:
                split_types.append(char_types[temp_type[0]:i])
                temp_type = (i, char_types[i][-1])
        if not split_types:
            split_types.append([char_data for char_data in char_types])
        else:
            split_types.append(char_types[-1][0])
        return split_types

    def _parse(self):
        if self.exp:
            char_types = []
            for char in self.exp:
                char_types.append((char, self.get_seq_type(char)))
            result = []
            split_chars = self._get_split_chars(char_types)
            for pack in split_chars:
                seq = ''
                if pack[0][-1] != 'operator':
                    for char_data in pack:
                        seq += char_data[0]
                    seq_type = self.get_seq_type(seq)
                    result.append(Token(seq, seq_type))
                else:
                    result.extend([Token(i[0], 'operator') for i in pack])
            return result

    @staticmethod
    def get_seq_type(s: str) -> str:
        if s.isdigit():
            return 'integer'
        elif s in TOKENS_TYPE:
            return TOKENS_TYPE[s]
        elif not s.split():
            return 'whitespace'
        elif len(s) > 1 and s[0] in ("'", '"') and (s[-1] in ("'", '"')):
            return 'string'
        return 'identifier'

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        if self.num <= len(self.parsed_exp):
            return self.parsed_exp[num]
        raise StopIteration
