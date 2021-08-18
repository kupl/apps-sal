class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.stack_position = 0

    def visit(self, url: str) -> None:
        self.stack_position += 1
        print(('You are in \"{}\". Visit \"{}\"'.format(self.stack[-1], url)))
        while self.stack_position < len(self.stack):
            self.stack.pop()
        self.stack.append(url)

    def back(self, steps: int) -> str:
        self.stack_position = max(0, self.stack_position - steps)
        if self.stack_position == 0:
            print('cant go any more back')
        return self.stack[self.stack_position]

    def forward(self, steps: int) -> str:
        self.stack_position = min(len(self.stack) - 1, self.stack_position + steps)
        if self.stack_position == len(self.stack) - 1:
            print('cant go any more forwards')
        return self.stack[self.stack_position]
