import collections
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        #remove duplicate if type3 exists remove type1 and type2
        type1_graph=collections.defaultdict(set)
        type2_graph=collections.defaultdict(set)
        type3_graph=collections.defaultdict(set)
        alice_graph=collections.defaultdict(set)
        bob_graph=collections.defaultdict(set)
        no_of_type1_edges=0
        no_of_type2_edges=0
        no_of_type3_edges=0
        for t,v1,v2 in edges:
            if t==3:
                type3_graph[v1].add(v2)
                type3_graph[v2].add(v1)
                alice_graph[v1].add(v2)
                alice_graph[v2].add(v1)
                bob_graph[v1].add(v2)
                bob_graph[v2].add(v1)
                no_of_type3_edges +=1

            if t==1:
                type1_graph[v1].add(v2)
                type1_graph[v2].add(v1)
                no_of_type1_edges +=1
                alice_graph[v1].add(v2)
                alice_graph[v2].add(v1)

            if t==2:
                type2_graph[v1].add(v2)
                type2_graph[v2].add(v1)
                no_of_type2_edges +=1
                bob_graph[v1].add(v2)
                bob_graph[v2].add(v1)

        def dfs(s,edges,visited):
            for e in edges[s]:
                if e not in visited:
                    visited.add(e)
                    dfs(e,edges,visited)


        def tran_graph(edges):
            nodes_set=[]
            total_visited=set()
            if len(edges)==0:
                return []
            for s in edges.keys():
                if s not in total_visited:
                    visited=set()
                    dfs(s,edges,visited)
                    nodes_set.append(visited)
                    total_visited|=visited
            print(nodes_set)
            return nodes_set
        # check whether alice and bob's graph connected
        for nodes_set in (tran_graph(alice_graph),tran_graph(bob_graph)):
            if len(nodes_set)!=1:
                return -1
            if len(nodes_set[0])!=n:
                return -1
        #remove duplicate type edge
        type3_nodes_sets=tran_graph(type3_graph)
        print(\"type3_nodes_sets\",type3_nodes_sets)
        print(\"type3 edges\",no_of_type3_edges)
        type3_nodes=0
        removed=no_of_type3_edges
        for set_ in type3_nodes_sets:
            type3_nodes+=len(set_)
            removed-=len(set_)-1
        print(removed)


        graphs=len(type3_nodes_sets)
        removed+=no_of_type1_edges-(graphs-1+n-type3_nodes)
        removed += no_of_type2_edges - (graphs - 1 + n - type3_nodes)
        # print(removed)
        return removed

