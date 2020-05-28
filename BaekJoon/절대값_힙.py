import sys
import heapq

numbers = int(input())
heap = []

# absolute heap
# push 할 때, Tuple 형태로 집어넣는다
# 앞에 있는 값으로 비교를 하기 때문에
# 절대 값이 제일 작을 숫자를 찾고
# 그 수의 실제 값을 출력한다.
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)