import sys
import heapq

numbers = int(input())
heap = []

# Max heap
# heappop() 함수가 가장 작은 값을 리턴하기 떄문에
# 가장 작은 값에 -1을 곱해서
# 가장 큰 수로 만들어서 출력

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)