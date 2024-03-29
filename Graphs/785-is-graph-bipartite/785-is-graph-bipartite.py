class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        N = len(graph)
        
        # TYPE 1) color = -1
        # TYPE 2) color = 1
        # not visited) color = 0
        colors = [0 for _ in range(N)]
        
        def bfs(start):
            queue = [start]
            colors[start] = 1
            
            while queue:
                here = queue.pop(0)
                
                for there in graph[here]:
                    if colors[there] != 0:
                        if colors[there] == colors[here]:
                            return False
                    else:
                        colors[there] = -colors[here]
                        queue.append(there)
            return True
        
        for start in range(N):
            if colors[start] != 0:
                continue
            if not bfs(start):
                return False
        return True

# hyebin's solution
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colored = {}
        
        for v in range(V):
            if v not in colored and graph[v]:
                colored[v] = 1
                
                queue = collections.deque([v])
                while queue:
                    here = queue.popleft()
                    for there in graph[here]:
                        if there not in colored:
                            colored[there] = -colored[here]
                            queue.append(there)
                        elif colored[there] == colored[here]:
                            return False
        return True