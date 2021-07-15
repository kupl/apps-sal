class InfiniTick:
    def __init__(self):
        self.mem = [0]
        self.pointer = 0
    
    def move_right(self):
        self.pointer += 1
        if self.pointer == len(self.mem):
            self.mem.append(0)
    
    def move_left(self):
        if self.pointer != 0:
            self.pointer -= 1
        else:
            self.mem.insert(0,0)
            self.pointer = 0

    def increment(self):
        self.mem[self.pointer] += 1
        if self.mem[self.pointer] > 255:
            self.mem[self.pointer] = 0
            
    def decrement(self):
        self.mem[self.pointer] -= 1
        if self.mem[self.pointer] < 0:
            self.mem[self.pointer] = 256 + self.mem[self.pointer]
            
    def output(self):
        return chr(self.mem[self.pointer])

    def process(self, tape):
        result = ""
        i = 0
        
        while True:
            if tape[i] == ">":
                self.move_right()
            elif tape[i] == "<":
                self.move_left()
            elif tape[i] == "+":
                self.increment()
            elif tape[i] == "-":
                self.decrement()
            elif tape[i] == "*":
                result += self.output()
            elif tape[i] == "&":
                break
            elif tape[i] == "/":
                if self.mem[self.pointer] == 0:
                    i += 1
            elif tape[i] == "\\":
                if self.mem[self.pointer] != 0:
                    i += 1
            i += 1
            if i == len(tape):
                i = 0
            elif i > len(tape):
                i = 1
                
        return result
        
def interpreter(tape):
    tick = InfiniTick()
    return tick.process(tape)
