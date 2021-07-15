def check_generator(gen):
    if not gen.gi_frame:
        return "Finished"
    if gen.gi_frame.f_lasti == -1:
        return "Created"
    return "Started"
