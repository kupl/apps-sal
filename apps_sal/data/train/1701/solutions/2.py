import re
from operator import add, sub, mul, floordiv, and_, or_, xor


class Machine(object):

    def __init__(self, cpu):
        self.cpu = cpu

    def reg_or_int(self, val):
        if val in 'abcd':
            return self.cpu.read_reg(val)
        return int(val)

    def stack_op(self, instr):
        # push reg|int
        match = re.fullmatch(r'push ([a-d]|\d+)', instr)
        if match:
            self.cpu.write_stack(self.reg_or_int(match.group(1)))
            return
        # pop [reg]
        match = re.fullmatch(r'pop( ([a-d]))?', instr)
        if match:
            val = self.cpu.pop_stack()
            if match.group(2):
                self.cpu.write_reg(match.group(2), val)
            return
        # pushr | pushrr | popr | poprr
        match = re.fullmatch(r'(push|pop)r(r)?', instr)
        if match:
            if match.group(1) == 'push':
                for reg in ('dcba' if match.group(2) else 'abcd'):
                    self.cpu.write_stack(self.cpu.read_reg(reg))
            else:
                for reg in ('abcd' if match.group(2) else 'dcba'):
                    self.cpu.write_reg(reg, self.cpu.pop_stack())
            return
        raise ValueError('Invalid instruction')

    def move_op(self, instr):
        # mov reg|int, reg2
        match = re.fullmatch(r'mov ([a-d]|\d+), ([a-d])', instr)
        if match:
            self.cpu.write_reg(match.group(2), self.reg_or_int(match.group(1)))
            return
        raise ValueError('Invalid instruction')

    def arith_op(self, instr):
        # add|sub|mul|div|and|or|xor[a] reg|int [reg]
        match = re.fullmatch(r'(add|sub|mul|div|and|or|xor)(a)? ([a-d]|\d+)(, ([a-d]))?', instr)
        if match:
            op = {'add': add, 'sub': sub, 'mul': mul, 'div': floordiv,
                  'and': and_, 'or': or_, 'xor': xor}[match.group(1)]
            if match.group(2):
                self.cpu.write_stack(self.cpu.read_reg('a'))
            operand_size = self.reg_or_int(match.group(3))
            save_reg = match.group(5) or 'a'
            val = self.cpu.pop_stack()
            for _ in range(1, operand_size):
                val = op(val, self.cpu.pop_stack())
            self.cpu.write_reg(save_reg, val)
            return
        raise ValueError('Invalid instruction')

    def execute(self, instr):
        if instr.startswith('p'):
            self.stack_op(instr)
        elif instr.startswith('mov'):
            self.move_op(instr)
        else:
            self.arith_op(instr)
