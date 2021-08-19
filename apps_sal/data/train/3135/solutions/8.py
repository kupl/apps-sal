def meeting_time(Ta, Tb, r):
    return f'{round(1 / abs(1 / Ta - 1 / Tb), 2):.2f}' if Ta and Tb else f'{max(abs(Ta), abs(Tb)):.2f}'
