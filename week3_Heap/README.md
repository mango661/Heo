# Week3 Heap 발표자료
- 12018 Yonsei TOTO

## [1. 12018 Yonsei TOTO](https://www.acmicpc.net/problem/12018)

![pa1](https://user-images.githubusercontent.com/87264787/127278733-2e7e4be2-3b90-46cd-b659-dd7c8d189514.png)


### 1.1 자료구조

1. mylect (max heap) : 내 강의를 담을 힙 자료구조
2. milege (min heap) : 수강 신청한 마일리지 점수를 저장한 힙 자료구조

→ mylect가 max heap인 경우 : 마일리지를 초과할 경우 큰 마일리지가 소모되는 강의를 우선적으로 제거하기 위함

### 1.2 풀이 과정

1. 신청인원(P)과 수강인원(L) 차이를 구해 마일리지와 함께 heap에 저장한다.

    - heap은 마일리지를 최소로 사용하므로 min heap을 기준으로 한다.

2. P-L이 0보다 작은 경우 마일리지는 1을 필요로 한다.

3. P-L이 0보다 크거나 같은 경우, P-L이 0이 될 때까지 milege를 꺼내면서 1씩 감소시킨다.

    - P-L이 0이 되면 마일리지에서 pop한 값을 mylect에 저장한다.

4. mylect에 담긴 마일리지 합이 m보다 클 경우 하나씩 pop해나간다.

5. 최종적으로 mylect에 남은 강의 수를 출력한다.

### 1.3 소스 코드

```python
#3190 뱀
#문제풀이  1. 방향 설정하는것은 코드 길어서 따로 함수로 편집
#2.디큐를 사용해서 시간 복잡도 감소
#3. 뱀의 위치를 2차원 배열을 통해 구현 + 사과의 위치를  1로 따로 표시해서 구현
#4 특정 위치 -> 방향전화  ==> 딕셔너리 사용
from collections import deque

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
```
