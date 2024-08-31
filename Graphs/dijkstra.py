class Graph:
    def __init__(self,edges) -> None:
        vertexes = set()
        for idx in edges:
            vertexes.add(idx[0])
            vertexes.add(idx[1])
        
        self.graph = [[] for _ in range(max(vertexes)+1)]
        
        for idx in edges:
            self.graph[idx[0]].append((idx[1],idx[2]))


    def dijkstra():
        pass
            
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
graph = Graph(edges)
print(graph.graph)
