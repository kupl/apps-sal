def complexSum(A): return (lambda s: {'1i': 'i', '-1i': '-i', '0i': '0'}.get(s, s))(str(sum(complex(x.replace('i', 'j'))for x in A)).replace('j', 'i').strip('()').replace('+0i', ''))
