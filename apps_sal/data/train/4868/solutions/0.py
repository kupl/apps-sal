import os


def get_output(s):
    return os.popen(s).read()
