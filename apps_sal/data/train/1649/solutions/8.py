import abc


class Condition(abc.ABC):

    @abc.abstractmethod
    def check_condition(self, params):
        pass


class ConditionEvent(Condition):

    def __init__(self, event_name):
        self.event_name = event_name

    def check_condition(self, params):
        event_name = params
        return self.event_name == event_name


class Transition:

    def __init__(self, fsm, to):
        self.fsm = fsm
        self.to = to
        self.conditions = []

    def check_conditions(self, params):
        return all((cond.check_condition(params) for cond in self.conditions))


class State:

    def __init__(self, fsm, name):
        self.name = name
        self.transitions = []

    def next_state(self, params):
        next_state = next((trans.to for trans in self.transitions if trans.check_conditions(params)), None)
        return next_state


class FSM:

    def __init__(self):
        self.cur_state_name = None
        self.states = {}

    def next_state(self, params):
        cur_state = self.states[self.cur_state_name]
        next_state = cur_state.next_state(params)
        if next_state is None:
            raise RuntimeError('Error')
        self.cur_state_name = next_state


def create_scheme():
    scheme_str = '\nCLOSED: APP_PASSIVE_OPEN -> LISTEN\nCLOSED: APP_ACTIVE_OPEN  -> SYN_SENT\nLISTEN: RCV_SYN          -> SYN_RCVD\nLISTEN: APP_SEND         -> SYN_SENT\nLISTEN: APP_CLOSE        -> CLOSED\nSYN_RCVD: APP_CLOSE      -> FIN_WAIT_1\nSYN_RCVD: RCV_ACK        -> ESTABLISHED\nSYN_SENT: RCV_SYN        -> SYN_RCVD\nSYN_SENT: RCV_SYN_ACK    -> ESTABLISHED\nSYN_SENT: APP_CLOSE      -> CLOSED\nESTABLISHED: APP_CLOSE   -> FIN_WAIT_1\nESTABLISHED: RCV_FIN     -> CLOSE_WAIT\nFIN_WAIT_1: RCV_FIN      -> CLOSING\nFIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT\nFIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2\nCLOSING: RCV_ACK         -> TIME_WAIT\nFIN_WAIT_2: RCV_FIN      -> TIME_WAIT\nTIME_WAIT: APP_TIMEOUT   -> CLOSED\nCLOSE_WAIT: APP_CLOSE    -> LAST_ACK\nLAST_ACK: RCV_ACK        -> CLOSED\n'
    scheme = []
    for line in scheme_str.splitlines():
        if not line:
            continue
        (from_state, rest) = line.split(':')
        (event, to_state) = rest.split('->')
        scheme.append((from_state.strip(), to_state.strip(), event.strip()))
    return scheme


def create_fsm(scheme):
    fsm = FSM()
    for (from_state_name, to_state_name, event) in scheme:
        try:
            state = fsm.states[from_state_name]
        except KeyError:
            state = fsm.states[from_state_name] = State(fsm, from_state_name)
        transtion = Transition(fsm, to=to_state_name)
        transtion.conditions.append(ConditionEvent(event))
        state.transitions.append(transtion)
    return fsm


def traverse_TCP_states(events):
    scheme = create_scheme()
    fsm = create_fsm(scheme)
    fsm.cur_state_name = 'CLOSED'
    try:
        for event in events:
            fsm.next_state(event)
    except:
        return 'ERROR'
    else:
        return fsm.cur_state_name
