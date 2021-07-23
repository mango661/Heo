#1158 좋은친구
#이렇게 하면 귀신 같이 시관 초과남 

#시간초과가 나는 이유 : for /for + 모든 경우의수 다검색 해서 그런듯

import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
inp = [len(input()) for i in range(N)]
num = [0 for i in range(22)]
print(inp)
cnt = 0
for i in range(3, 22):
    q = deque()
    for leng in inp:
        print(leng,num,cnt)
        q.append(leng)
        if len(q) > K + 1:
            if q.popleft() == i: 
                num[i] -= 1
        if leng == i:
            if num[i] > 0:
                 cnt += num[i]
            num[i] += 1
    
print(cnt)    

#https://yongjoonseo.dev/problem%20solving/PS-baekjoon032/

#https://ihatecucumber.tistory.com/46