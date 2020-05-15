TC = int(input())
num = [i for i in range(1, 13)]
Len = len(num)

# 부분집합 구하기
# 부분집합을 리스트에 다 담음
lst = []
for i in range(1 << Len):
    sub_lst = []
    for j in range(Len):
        if i & (1 << j):
            sub_lst.append(num[j])
    lst.append(sub_lst)

for tc in range(1, TC+1):
    N, K = map(int, input().split())

    # 길이 맞는 리스트 구하기
    len_lst = []
    for i in lst:
        if len(i) == N:
            len_lst.append(i)

    # 합 일치 유무 확인
    result = 0
    for i in len_lst:  # i가 리스트니까.
        if(sum(i) == K):
            result += 1

    print("#%s %d" % (tc, result))
