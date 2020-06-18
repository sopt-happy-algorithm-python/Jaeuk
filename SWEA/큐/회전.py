# N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    for i in range(m):
        queue.append(queue.pop(0))

    print("#%s %d" % (t, queue[0]))