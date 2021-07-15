def check_generator(gen):
    if gen.gi_frame != None:
        if len(gen.gi_frame.f_locals.keys()) == 1:
            return 'Created'
        else:
            return 'Started'
    if gen.gi_frame == None:
        return 'Finished'
