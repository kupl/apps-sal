import sys


class Machine:
    def __init__(self):
        self._actions = [lambda x:x + 1, lambda x:0, lambda x: x / 2, lambda x: x * 100, lambda x: x % 2]
        self.action_mapping = {}
        self.last = 0

    def command(self, cmd, num):
        self.last = cmd
        if cmd not in self.action_mapping:
            self.action_mapping[cmd] = 0
        return self._actions[self.action_mapping[cmd]](num)

    def response(self, res):
        if not res:
            self.action_mapping[self.last] += 1
