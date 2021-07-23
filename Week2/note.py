# 요세푸스 문제

# 1 . 원형 큐 느낌으로 문제 풀이 시작

# 2. 삭제시 삭제한 부분 부터 1번째로 리셋

#3 .출력하는거 list 랑 디큐 차이로 안되는거 같은데 생각해보기
# print("<"+", ".join(str(e) for e in ans)+">")
#리스트로 비교


from collections import deque


N,K = map(int,input().split())

arr = deque([i for i in range(1,N+1,1)])
ans = deque()

for j in range(N):
    for p in range(K-1):
        arr.append(arr.popleft())
    ans.append(arr.popleft())


print("<", end='')
for i in ans:
    if i == ans[-1]:
        print(i, end = '')
    else:
        print("%d, " %(i), end='')
print(">")


 #3190 뱀
#문제풀이 

#1. 
from collections import deque
from typing import Coroutine
arr = []
snake = deque()
Dir = {}
N = int(input().strip())
Location = [[0 for _ in range(N)]for _ in range(N)]
Ap = int(input().strip())
for i in range(Ap):
    a,b = map(int,input().split())
    Location[a-1][b-1] = 7
#지도 형태 구현을 위해 2차원배열 이용,사과위치를 7로 구현
Di = int(input().strip())
for j in range(Di):
    a,b = input().split()
    Dir[int(a)] = b
#시간 입력시 방향을 도출해 내기 위해 DIC 사용

def Direction(move,D):
    x,y = move
    if x == 0:
        if D == 'D':
            if y>0:
                return(-1,0)
            else:
                return(1,0)
        else:
            if y>0:
                return(1,0)
            else:
                return(-1,0)
    elif y ==0:
        if D =='D':
            if x>0:
                return(0,1)
            else:
                return(0,-1)
        else:
            if x>0:
                return(0,-1)
            else:
                return(0,1)

Location[0][0] = 1
x,y = 0,0
time = 0
move = (1,0)
snake.appendleft((0,0))

while True:
    time = time + 1
    
    a,b = move
    x,y = x+a,y+b
    
    if 0 <= x < N and 0 <= y <N:
        if Location[y][x] == 7:
            snake.appendleft((y,x))
           
            Location[y][x] = 1
        elif Location[y][x] ==0:
            
            Location[y][x] = 1
            snake.appendleft((y,x))
            a,b = snake.pop()
            Location[a][b] = 0
        elif Location[y][x] == 1:
            
            break
        if time in Dir:
            
            move = Direction(move,Dir[time])
    else:
        break
print(time)

#3 큐2
import sys
input = sys.stdin.readline

from collections import deque

N = int(input().strip())
arr = []
ans = deque()
for i in range(N):
    arr = input().split()
    
    if arr[0] == "push":
        ans.append(arr[1])
    elif arr[0] =="pop":
        if not ans:
            print("-1")
        else:
            print(ans.popleft())
    elif arr[0] == "size":
        print(len(ans))
    elif arr[0] == "empty":
        if ans :
            print("0")
        else:
            print("1")
    elif arr[0] == "front":
        if not ans:
            print("-1")
        else:
             print(ans[0])
    elif arr[0] == "back":
        if not ans:
                print("-1")
        else:
             print(ans[-1])


             
#1158 좋은친구


from collections import deque

N,K = map(int,input().split())
arr = []
answer = 0
for i in range(N):
    arr.append(len(input().strip()))
    
num = [0 for i in range(22)]


for i in range(3, 22):
    arr2 = deque()
    for word in arr:
        arr2.append(word)
        if len(arr2) > K + 1:
            if arr2.popleft() == i: 
                num[i] -= 1
        if word == i:
            if num[i] > 0:
                 answer += num[i]
            num[i] += 1
    
print(answer)    

#금) 1927 최소 힙 / 11000 강의실배정

#시간 줄이기 - > import / readline

import sys
import heapq
input = lambda:sys.stdin.readline().strip()
ans = []

N = int(input().strip())

for i in range(N):
    A = int(input().strip())

    if A > 0:
        heapq.heappush(ans,A)
    elif A == 0:
        if ans:
            print(heapq.heappop(ans))
        else:
            print("0")

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