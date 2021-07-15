def tiaosheng(failed_counter):
    jump = 60
    for failed in failed_counter:
        if failed < jump:
            jump -= min(jump - failed, 3)
    return jump
