def can_i_play(now_hour, start_hour, end_hour):
  if end_hour < start_hour: end_hour += 24
  return start_hour<= now_hour < end_hour or start_hour<= now_hour+24 < end_hour

