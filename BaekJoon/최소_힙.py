import sys
import heapq

numbers = int(input())
heap = []

#Min heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)