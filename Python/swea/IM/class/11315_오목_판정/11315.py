
di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

def f(N):
    for i in range(N): #돌이 어딘지는 모르니 다돌아봐
        for j in range(N):
            for k in range(4):
                cnt = 0
                ni, nj = i, j # 돌인지 확인할 위치
                while 0<=ni<N and 0<=nj<N and matrix[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    ni += di[k]
                    nj += dj[k]
    return 'NO'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [input() for _ in range(N)]
    ans = f(N)
    print(f'#{tc} {ans}')