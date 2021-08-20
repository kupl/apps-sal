import subprocess
import os


def get_output(Q):
    return ''.join(os.popen(Q).readlines())
