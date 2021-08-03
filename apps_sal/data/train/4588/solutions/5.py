class State:
    def __init__(self):
        pass


class PausedIncreasing(State):
    @classmethod
    def handle(cls, e, val):
        nextstate = cls
        if e == '.':
            pass
        elif e == 'P':
            val += 1
            nextstate = MovingIncreasing
        elif e == 'O':
            nextstate = PausedDecreasing
        return val, nextstate


class PausedDecreasing(State):
    @classmethod
    def handle(cls, e, val):
        nextstate = cls
        if e == '.':
            pass
        elif e == 'P':
            val -= 1
            nextstate = MovingDecreasing
        elif e == 'O':
            nextstate = PausedIncreasing
        return val, nextstate


class MovingIncreasing(State):
    @classmethod
    def handle(cls, e, val):
        nextstate = cls
        if e == '.':
            val += 1
        elif e == 'P':
            nextstate = PausedIncreasing
        elif e == 'O':
            val -= 1
            nextstate = MovingDecreasing
        return val, nextstate


class MovingDecreasing(State):
    @classmethod
    def handle(cls, e, val):
        nextstate = cls
        if e == '.':
            val -= 1
        elif e == 'P':
            nextstate = PausedDecreasing
        elif e == 'O':
            val += 1
            nextstate = MovingIncreasing
        return val, nextstate


class GarageDoor:
    def __init__(self):
        self.val = 0
        self.state = PausedIncreasing

    def handle(self, e):
        self.val, self.state = self.state.handle(e, self.val)
        if self.val == 0:
            self.state = PausedIncreasing
        elif self.val == 5:
            self.state = PausedDecreasing
        return str(self.val)

    def get_output(self, events):
        return ''.join(str(self.handle(e)) for e in events)


def controller(events):
    gd = GarageDoor()
    return gd.get_output(events)
