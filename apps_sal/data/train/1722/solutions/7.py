from collections import defaultdict


class Machine:
    def __init__(self):
        self.translate = defaultdict(int)
        self.last_cmd = None

    def command(self, cmd, num):
        self.last_cmd = cmd
        return _actions[self.translate[cmd]](num)

    def response(self, res):
        if not res:
            self.translate[self.last_cmd] += 1
