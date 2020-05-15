row = 9
column = 9
bigBox = [[0 for i in range(row)] for j in range(column)]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    boxCount = int(input())
    for i in range(boxCount):
        box = list(map(int, input().split()))
        bigBox[box[0]:box[3]+1] = 1
        print(bigBox)

# 1
# 2
# 2 2 4 4 1