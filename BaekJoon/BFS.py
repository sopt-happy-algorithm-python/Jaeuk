def bfs(v, nodes):
    answer = []

    visited = [False] * 100001
    q = [v]

    while q:
        q.sort()
        for _ in range(len(q)):
            v = q.pop(0)
            if not (visited[v]):
                visited[v] = True
                answer.append(v)
                for i in nodes:
                    if i[0] == v:
                        print(i)
                        q.append(i[1])
    print(answer)


n, m, v = map(int, input().split())
nodes = []

for _ in range(m):
    nodes.append(list(map(int, input().split())))
print(nodes)

for i in range(len(nodes)):
    nodes[i].sort()
print(nodes)
bfs(v, nodes)

