#금) 11000 강의실배정

#시간 줄이기 - > import / readline
import sys
input = lambda:sys.stdin.readline().strip()
import heapq

arr = []

N = int(input().strip())
for i in range(N):
    arr.append(list(map(int,input().split())))   
arr.sort()

ans = []
heapq.heappush(ans,arr[0][1])

for i in range(1,N):


    if ans[0] > arr[i][0] :
        heapq.heappush(ans,arr[i][1])
    else:
        heapq.heappop(ans)
        heapq.heappush(ans,arr[i][1])


print(len(ans))