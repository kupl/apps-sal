def capital(capitals):
        return list(map(lambda val: 'The capital of ' + (val.get('state') or val.get('country')) + ' is ' + val["capital"],
                    capitals))
