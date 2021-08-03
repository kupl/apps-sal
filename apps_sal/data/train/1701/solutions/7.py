import operator


class Machine(object):

    def __init__(self, cpu):
        self.cpu = cpu
        self.registers = ['a', 'b', 'c', 'd']
        self.operations = {'add': operator.add, 'adda': operator.add,
                           'sub': operator.sub, 'suba': operator.sub,
                           'mul': operator.mul, 'mula': operator.mul,
                           'div': operator.truediv, 'diva': operator.truediv,
                           'and': operator.and_, 'anda': operator.and_,
                           'or': operator.or_, 'ora': operator.or_,
                           'xor': operator.xor, 'xora': operator.xor}

    def execute(self, instr):
        instr_list = instr.split()
        command = instr_list[0]
        if command == 'push':
            val = int(instr_list[1]) if instr_list[1].isdigit() else self.cpu.read_reg(instr_list[1])
            self.cpu.write_stack(val)

        elif command == 'pop':
            val = self.cpu.pop_stack()
            if len(instr_list) == 2:
                reg_name = instr_list[1]
                self.cpu.write_reg(reg_name, val)

        elif command == 'pushr':
            for reg in self.registers:
                val = self.cpu.read_reg(reg)
                self.cpu.write_stack(val)

        elif command == 'pushrr':
            for reg in self.registers[::-1]:
                val = self.cpu.read_reg(reg)
                self.cpu.write_stack(val)

        elif command == 'popr':
            for reg in self.registers[::-1]:
                val = self.cpu.pop_stack()
                self.cpu.write_reg(reg, val)

        elif command == 'poprr':
            for reg in self.registers:
                val = self.cpu.pop_stack()
                self.cpu.write_reg(reg, val)

        elif command == 'mov':
            first_el = instr_list[1][:-1]
            if first_el.isdigit():
                self.cpu.write_reg(instr_list[2], int(first_el))
            else:
                val = self.cpu.read_reg(first_el)
                self.cpu.write_reg(instr_list[2], val)

        else:
            if instr_list[1][-1] == ',':
                first_el = instr_list[1][:-1]
                destination_reg = instr_list[2]
            else:
                first_el = instr_list[1]
                destination_reg = 'a'
            if command[-1] == 'a':
                self.cpu.write_stack(self.cpu.read_reg('a'))

            start_op = self.cpu.pop_stack()
            how_many = int(first_el) if first_el.isdigit() else self.cpu.read_reg(first_el)
            for i in range(how_many - 1):
                start_op = self.operations[command](start_op, self.cpu.pop_stack())
            self.cpu.write_reg(destination_reg, int(start_op))
