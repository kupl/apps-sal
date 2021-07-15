def get_output(s):
    import subprocess
    return subprocess.check_output(s.split()).decode('ascii')
