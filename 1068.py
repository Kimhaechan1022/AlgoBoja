import sys
input = sys.stdin.readline

# 깊이우선 탐색
# 처음 받은 인덱스의 배열값 = -2 초기화, root가 -1이라서
# 모든 재귀이후 삭제될 노드는 전부 -2로 초기화되어있음, -2가 아니면서 다른 노드의 부모 노드도 아닌,
# 즉 리프노드를 찾을떄 마다 카운트 +1
def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())


dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)