def Xbonacci(signature, n):
    def gen_bonacci(signature):
        yield from signature
        from collections import deque
        signature = deque(signature)
        while 1:
            signature.append(sum(signature))
            signature.popleft()
            yield signature[-1]
    from itertools import islice
    return [i for i in islice(gen_bonacci(signature), n)]
