def args_count(*args, **kwargs):
    return len(locals()['args']) + len(locals()['kwargs'])
