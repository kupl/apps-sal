class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans , invalid = [ ] , [ ]
        for t in transactions :
            trans += t.split( ',' ) ,
        trans.sort( key = lambda x : int( x[ 1 ] ) )
        invalid = set()
        for i in range( len( trans ) ) :
            if int( trans[ i ][ 2 ] ) > 1000 :
                invalid.add( ','.join( trans[ i ] ) )
                if i :
                    j = i
                    while j and int( trans[ i ][ 1 ] ) - int( trans[ j - 1 ][ 1 ] ) < 61 :
                        if trans[ i ][ 0 ] == trans[ j - 1 ][ 0 ] and trans[ i ][ 3 ] != trans[ j - 1 ][ 3 ] :
                            invalid.add( ','.join( trans[ j - 1 ] ) )
                        j -= 1

            elif i and int( trans[ i ][ 1 ] ) - int( trans[ i - 1 ][ 1 ] ) < 61 :
                j = i
                while j and int( trans[ i ][ 1 ] ) - int( trans[ j - 1 ][ 1 ] ) < 61 :                    
                    if trans[ i ][ 0 ] == trans[ j - 1 ][ 0 ] and trans[ i ][ 3 ] != trans[ j - 1 ][ 3 ] :
                        invalid.add( ','.join( trans[ j - 1 ] ) )
                        invalid.add( ','.join( trans[ i ] ) )
                    j -= 1
        return invalid
    #Sanyam Rajpal

