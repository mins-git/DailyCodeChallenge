import sys

sys.stdin = open('input.txt')


# Testcase 수

# 위 > 아래 1번부터 번호가 붙여있고 왼 > 오

# 가로 세로길이, 잘라야할 점선들. 가장큰 종이 조각 몇cm2?


row, col = map(int,input().split())
cut_count = int(input())
cut_list = [list(map(int, input().split())) for _ in range(cut_count)] #[[0, 3], [1, 4], [0, 2]]
matrix = [[0] * row for _ in range(col)]

# 0은 가로로자르기
# 1은 세로로자르기
result = 0
result_arr = []
# 가장 큰 넓이 추출.
for r, c in cut_list:
    # 만약 가로라면
