import re
FSM_STR = '\nCLOSED: APP_PASSIVE_OPEN -> LISTEN\nCLOSED: APP_ACTIVE_OPEN  -> SYN_SENT\nLISTEN: RCV_SYN          -> SYN_RCVD\nLISTEN: APP_SEND         -> SYN_SENT\nLISTEN: APP_CLOSE        -> CLOSED\nSYN_RCVD: APP_CLOSE      -> FIN_WAIT_1\nSYN_RCVD: RCV_ACK        -> ESTABLISHED\nSYN_SENT: RCV_SYN        -> SYN_RCVD\nSYN_SENT: RCV_SYN_ACK    -> ESTABLISHED\nSYN_SENT: APP_CLOSE      -> CLOSED\nESTABLISHED: APP_CLOSE   -> FIN_WAIT_1\nESTABLISHED: RCV_FIN     -> CLOSE_WAIT\nFIN_WAIT_1: RCV_FIN      -> CLOSING\nFIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT\nFIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2\nCLOSING: RCV_ACK         -> TIME_WAIT\nFIN_WAIT_2: RCV_FIN      -> TIME_WAIT\nTIME_WAIT: APP_TIMEOUT   -> CLOSED\nCLOSE_WAIT: APP_CLOSE    -> LAST_ACK\nLAST_ACK: RCV_ACK        -> CLOSED\n'.strip()
FSM = {(m.group(1), m.group(2)): m.group(3) for m in (re.fullmatch('(\\w+):\\s+(\\w+)\\s+->\\s+(\\w+)', a) for a in FSM_STR.split('\n'))}


def traverse_TCP_states(events):
    state = 'CLOSED'
    for e in events:
        state = FSM.get((state, e), 'ERROR')
    return state
