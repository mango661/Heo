

import heapq


a = []

heapq.heappush(a,50)
heapq.heappush(a,10)
heapq.heappush(a,20)

a.append(4)

print(a)

heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

print(max_heap)

max_item = heapq.heappop(max_heap)[1]
print(max_item)
 
 heapq.heapify -> 기존 정렬을 heap구조로

max heap -> heapq.heapq.heappush(a , - i) 구현  or 튜플

우선순위큐 구현
