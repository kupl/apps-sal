def processes(start, end, procs):
    def _p(start, end, procs, re_):
        for step in procs:
            res = re_[:]
            if step[1] == start:
                res.append(step[0])

                _p(step[2], end, [x for x in procs if x != step], res)

                if step[2] == end:
                    _p.gres.append(res);


    _p.gres = []
    _p(start, end, procs, [])
    return min(_p.gres, key=lambda x: len(x)) if _p.gres else []

