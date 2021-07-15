class CustomStack:

    def __init__(self, maxSize: int):
        \"\"\"
        ptr points to the last recently filled element, or -1 if empty
        \"\"\"
        self.stack = [None] * maxSize
        self.ptr = -1

    def push(self, x: int) -> None:
        \"\"\"
        Initial offset of every push is 0
        \"\"\"
        if self.ptr != len(self.stack) - 1:
            self.ptr += 1
            self.stack[self.ptr] = [x, 0]


    def pop(self) -> int:
        if self.ptr == -1:
            return -1
        else:
            # Get the number added with its offset
            num = self.stack[self.ptr][0] + self.stack[self.ptr][1]
            
            # Propagate this offset down to the next element
            if self.ptr != 0:
                self.stack[self.ptr - 1][1] += self.stack[self.ptr][1]
            self.ptr -= 1
            
            return num

    def increment(self, k: int, val: int) -> None:
        \"\"\"
        Mark where in the stack to propagate offset downwards
        \"\"\"
        if self.ptr == -1:
            return
        elif k > self.ptr:
            self.stack[self.ptr][1] += val
        else:
            self.stack[k - 1][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
