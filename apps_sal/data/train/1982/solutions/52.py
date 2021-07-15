class Solution:
    def possibleBipartition(self, N, dislikes):
        NOT_COLORED, BLUE, GREEN = 0, 1, -1 # Constant defined for color drawing to person
        def helper( person_id, color ):
            color_table[person_id] = color # Draw person_id as color
            for the_other in dislike_table[ person_id ]: # Draw the_other, with opposite color, in dislike table of current person_id
                if color_table[the_other] == color: # the_other has the same color of current person_id
                    return False
                if color_table[the_other] == NOT_COLORED and (not helper( the_other, -color)):
                    # Other people can not be colored with two different colors. 
\t\t\t\t\t# Therefore, it is impossible to keep dis-like relationship with bipartition.
                    return False
                    
            return True
\t\t
        
        # each person maintain a list of dislike
        dislike_table = collections.defaultdict( list )
        
        # cell_#0 is dummy just for the convenience of indexing from 1 to N
        color_table = [ NOT_COLORED for _ in range(N+1) ]
        
        for p1, p2 in dislikes:
            
            # P1 and P2 dislike each other
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
            
        
        # Try to draw dislike pair with different colors in DFS
        for person_id in range(1, N+1):
            
            if color_table[person_id] == NOT_COLORED and (not helper( person_id, BLUE)):
                # Other people can not be colored with two different colors. 
\t\t\t\t# Therefore, it is impossible to keep dis-like relationship with bipartition.
                return False 
        
        return True

