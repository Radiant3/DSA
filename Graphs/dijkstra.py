from queue import PriorityQueue

class Graph:
    def __init__(self,edges) -> None:
        vertexes = set()
        for idx in edges:
            vertexes.add(idx[0])
            vertexes.add(idx[1])
        
        self.numVertexes = max(vertexes)+1

        self.graph = [[0 for _ in range(self.numVertexes)] for _ in range(self.numVertexes)]
        
        for idx in edges:
            self.graph[idx[0]][idx[1]] = idx[2]
        print(self.graph)
        

    def dijkstra(self,source):
        distances = [float('inf') for _ in range(self.numVertexes)]
        prev = [0 for _ in range(self.numVertexes)]
        
        distances[source] = 0 
        queue = PriorityQueue()
        queue.put(source,0)
        
        while queue:
            vertex, weight = queue.get()

            if distances[vertex] == weight:
                for e in self.graph[vertex]:
                    pass

            
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
graph = Graph(edges)
print(graph.graph)
