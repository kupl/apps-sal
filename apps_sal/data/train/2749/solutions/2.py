solve = lambda a:'R'*([min(a),max(a)]!=sorted(a[0::len(a)-1])) + ['D','A'][a[-1]-a[-2]>0]
