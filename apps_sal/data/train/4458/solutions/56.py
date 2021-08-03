def time_correct(t):
    if t == '':
        return t
    if not t or len(t.split(':')) != 3:
        return None
    elif any((not i.isdigit() for i in t.replace(':', ''))):
        return None
    elif any((len(i) != 2 for i in t.split(':'))):
        return None
    else:
        h, m, s = list(map(int, t.split(':')))
        if m < 60 and s < 60 and h < 24:
            return t
        else:
            s_1 = s % 60
            s_2 = s // 60
            m_1 = (s_2 + m) % 60
            m_2 = (s_2 + m) // 60
            h_1 = h + m_2 if (h + m_2) < 24 else (h + m_2) % 24
            return '{:02d}:{:02d}:{:02d}'.format(h_1, m_1, s_1)
