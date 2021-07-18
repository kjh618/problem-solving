from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)] # vertex number starts from 1
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for vs in graph:
    vs.sort()


def dfs(current, visited):
    if current in visited:
        return

    visited.add(current)
    print(current, end=' ')

    for next in graph[current]:
        dfs(next, visited)


def bfs(start, discovered):
    q = deque()
    discovered.add(start)
    q.append(start)

    while len(q) > 0:
        current = q.popleft()
        print(current, end=' ')

        for next in graph[current]:
            if next not in discovered:
                discovered.add(next)
                q.append(next)


dfs(v, set())
print()
bfs(v, set())
print()
