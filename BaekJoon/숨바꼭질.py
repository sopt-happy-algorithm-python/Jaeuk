def bfs(v):
    # global K
    visited = [False]*100001
    q = [v]
    cnt = 0
    state = False

    while q:
        for _ in range(len(q)):
            v = q.pop(0)
            if not(visited[v]):
                visited[v] = True
                if v == K:
                    state = True
                    break
                if v-1 >= 0:
                    q.append(v-1)
                if v+1 <= 100000:
                    q.append(v+1)
                if v*2 <= 100000:
                    q.append(v*2)
        if state:
            print(cnt)
            break
        cnt += 1


N, K = map(int, input().split())
bfs(N)