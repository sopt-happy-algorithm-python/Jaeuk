TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = list(map(int, input().split()))
    lst = [0]*N

    # Max 값 구하기
    for i in range(N//2):
        lst[i*2] = max(Data)
        Data.pop(Data.index(max(Data)))

    for i in range(N//2):
        lst[i*2+1] = min(Data)
        Data.pop(Data.index(min(Data)))

    print('#%s'%tc, end=' ')
    for i in range(10):
        print(lst[i], end=" ")
    print()