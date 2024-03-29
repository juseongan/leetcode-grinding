# hyochan's solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        N = len(graph)
        paths = []

        def dfs(here, path):
            if here == N-1:
                paths.append(path)
                print(path)

            for there in graph[here]:
                dfs(there, path + [there])

        dfs(0, [0])

        return paths




# hyebin's solution
# iteractive (stack) -> Wrong
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1 
        path = [] 
        visited = []

        def dfs(source, target, visited):
            visited.append(source)
            if source == target:
                path.append(visited.copy())

            for adjacent_vertex in graph[source]:
                dfs(adjacent_vertex, target, visited)

            visited.pop()
            return path

        return dfs(0, target, visited)