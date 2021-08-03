def make_readable(seconds):
    hours = seconds // 3600
    mins = (seconds - hours * 3600) // 60
    secs = seconds - (hours * 3600 + mins * 60)

    h_str = str(hours)
    m_str = str(mins)
    s_str = str(secs)

    if len(h_str) < 2:
        h_str = '0' + h_str

    if len(m_str) < 2:
        m_str = '0' + m_str

    if len(s_str) < 2:
        s_str = '0' + s_str

    return(f'{h_str}:{m_str}:{s_str}')
