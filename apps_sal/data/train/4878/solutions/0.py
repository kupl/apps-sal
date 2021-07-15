def check_generator(gen):
  if gen.gi_frame is None:
    return "Finished"
  if gen.gi_frame.f_lasti == -1:
    return "Created"
  return "Started"
