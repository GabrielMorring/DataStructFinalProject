from collections import deque

def queue(list, append):
    queue = deque(list)
    queue.append(append)
    queue.popleft()
    return queue

# tests
print(queue([1,2,3,4,5], 6)) # 2,3,4,5,6

print(queue([10,11], 20)) # 11,20