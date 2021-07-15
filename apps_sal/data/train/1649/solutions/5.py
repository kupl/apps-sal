NEW_STATE = {
"CLOSED__APP_PASSIVE_OPEN" : "LISTEN",
"CLOSED__APP_ACTIVE_OPEN"  : "SYN_SENT",
"LISTEN__RCV_SYN"          : "SYN_RCVD",
"LISTEN__APP_SEND"         : "SYN_SENT",
"LISTEN__APP_CLOSE"        : "CLOSED",
"SYN_RCVD__APP_CLOSE"      : "FIN_WAIT_1",
"SYN_RCVD__RCV_ACK"        : "ESTABLISHED",
"SYN_SENT__RCV_SYN"        : "SYN_RCVD",
"SYN_SENT__RCV_SYN_ACK"    : "ESTABLISHED",
"SYN_SENT__APP_CLOSE"      : "CLOSED",
"ESTABLISHED__APP_CLOSE"   : "FIN_WAIT_1",
"ESTABLISHED__RCV_FIN"     : "CLOSE_WAIT",
"FIN_WAIT_1__RCV_FIN"      : "CLOSING",
"FIN_WAIT_1__RCV_FIN_ACK"  : "TIME_WAIT",
"FIN_WAIT_1__RCV_ACK"      : "FIN_WAIT_2",
"CLOSING__RCV_ACK"         : "TIME_WAIT",
"FIN_WAIT_2__RCV_FIN"      : "TIME_WAIT",
"TIME_WAIT__APP_TIMEOUT"   : "CLOSED",
"CLOSE_WAIT__APP_CLOSE"    : "LAST_ACK",
"LAST_ACK__RCV_ACK"        : "CLOSED" }


def traverse_TCP_states(events, state="CLOSED"):
    for event in events:
        QUERY = "%s__%s" % (state, event)
        if QUERY in NEW_STATE:
            state = NEW_STATE[QUERY]
        else:
            return "ERROR"
    
    return state
