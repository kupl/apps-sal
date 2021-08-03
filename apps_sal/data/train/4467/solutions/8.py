from enum import Enum

State = Enum('State', 'NONE SEEN APPENDED')


def remember(str_):
    states = {}
    result = []
    for c in str_:
        state = states.get(c, State.NONE)
        if state is State.NONE:
            states[c] = State.SEEN
        elif state is State.SEEN:
            result.append(c)
            states[c] = State.APPENDED
    return result
