def what_is_the_time(time_in_mirror):
    hours, minutes = map(int, time_in_mirror.split(':'))
    m_hours, m_minutes = divmod(720 - 60 * hours - minutes, 60)
    return '{:02}:{:02}'.format(m_hours + 12 * (m_hours <= 0), m_minutes)
