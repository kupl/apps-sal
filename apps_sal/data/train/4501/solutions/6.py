inside_out=lambda s:" ".join([i[:len(i)//2][::-1] + ["",i[len(i)//2]][len(i)&1] + i[len(i)//2+(len(i)&1):][::-1] for i in s.split()])
