get_output = lambda c, o=__import__("os"): o.popen(c).read()
