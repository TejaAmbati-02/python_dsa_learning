def length_of_string(name):
    cnt = 0
    for ele in name:
        cnt +=1 
    return cnt

name = "Teja12345"
print(length_of_string(name))
print(len(name))

arr = [1,5,6,7,4]
print(sorted(arr))
print(sorted(arr, reverse=True))
print(arr)

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)
print("==")
arr = [-1,5,-6,7,4]
print(sorted(arr, key= lambda x: abs(x)))
print("==")
arr = [-1,5,-6,7,4]
arr.sort(key=abs)
print(arr)
print("==")
fruits_list = ['apple', 'pineapple','kiwi']
print(sorted(fruits_list, key=len))
print("==")
print(sorted(fruits_list, key=len, reverse=True))
print("===")

arr = [5,6,8,7]
print(min(arr))
print(max(arr))
arr = [-15,6,8,7]
print(min(arr))
print(max(arr))

arr = [-15,6,8,7]
print(abs(min(arr)))
print(abs(max(arr)))


arr = [-15,6,8,7]
print(min(arr, key=abs))
print(max(arr, key = abs))

fruits_list = ['apple', 'pineapple','kiwi']
print(max(fruits_list, key=len))
print(min(fruits_list, key=len))


print(sum(arr))

arr = [15,6,8,7]
print(sum(arr)) # 0 + 15 + 6 + 8 + 7

arr = [15,6,8,7]
print(sum(arr, start=10)) # 10 + 15 + 6 + 8 + 7



arr = [15,6,8,7]
import math
print(math.prod(arr))
print(len(arr))

arr = [True, False, True]
print(any(arr))
print(all(arr))
arr = [1,6,1,7]
print(arr.count(1))

def count_ele_list(arr, num):
    count = 0
    for i in arr:
        if num == i:
            count += 1
    return count

print(count_ele_list(arr, 1))

arr = [5,6,1,7]
for index, value in enumerate(arr):
    print(index, value)

print(list(enumerate(arr)))

arr = [5,6,1]
print(list(reversed(arr)))
print(arr)

arr = list(range(5))
print(arr)

arr = list(range(2, 5))
print(arr)

arr = list(range(2, 15, 3))
print(arr)

from collections import deque # Used in Stack & Queue, Fast operation from front & End 
dq = deque([2,3,1])

dq.append(5)
print(dq)

dq.appendleft(7)
print(dq)

print(dq.pop())
print(dq)

print(dq.popleft())
print(dq)

dq.extend([10, 19])
print(dq)

dq.extend([10, "teja"])
print(dq)

dq.extendleft([89, "Teja"])
print(dq)

dq.rotate(1)
print(dq)

dq.rotate(2)
print(dq)

dq.rotate(7)
print(dq)

print(len(dq))


from collections import Counter
arr = Counter([1,2,2,3,2,3,3,4]) # 1 -> 1, 2 -> 3, 3 -> 3, 4 -> 1

print(arr[1])
print(arr[2])
print(arr[10])

print(arr.most_common(1))
print(arr.most_common(2))
print(arr.most_common(3))
print(arr.most_common(4))

print(list(arr.elements()))

arr.update([7])
print(list(arr.elements()))

arr.update([7, 7])
print(list(arr.elements()))

arr.update([7, 3])
print(list(arr.elements()))

arr.subtract([3])
print(list(arr.elements()))

arr.subtract([3, 3])
print(list(arr.elements()))


arr.subtract([3, 3, 100])
print(list(arr.elements()))

c1 = Counter([1,2,2,3,2,3,3,4]) # 1 -> 1, 2 -> 3, 3 -> 3, 4 -> 1
c2 = Counter([3,3,1,4,5])
used in Count Frequency
c3 = c1 - c2
print(c3)
print(list(c3.elements()))

c3 = c2 - c1
print(c3)
print(list(c3.elements()))


c3 = c1 + c2
print(c3)
print(list(c3.elements()))

c3 = c2 + c1
print(c3)
print(list(c3.elements()))

c3 = c1 & c2
print(c3)
print(list(c3.elements()))

c3 = c2 & c1
print(c3)
print(list(c3.elements()))

c3 = c1 | c2
print(c3)
print(list(c3.elements()))

c3 = c2 | c1
print(c3)
print(list(c3.elements()))

from collections import defaultdict

dd = defaultdict(int) # Always create a defualt value not give key error if key not present
dd[1] = 'teja'
dd['sai'] = 'teja'
dd['t'] = 99
dd['list'] = [1,2,4]
print(dd)
print(dd['list'])
print(dd['xyz'])
dd[1,5,6] = "john"
print(dd[1,5,6])
dd['teja'] = [7,8,9]
dd['teja'].append(10)
print(dd['teja'])



# Hasing, LRU Cache
from collections import OrderedDict

od = OrderedDict([(1, "a"), (3, "b"), (2, "c"), (7, "d")])
print(od)
print(od[1])
print(od[10])
if 10 in od:
    print(od[10])
else:
    print("Not in dict")

# print(od)

od[10] = "j"
print(od)


od.move_to_end(1)
print(od)

od.move_to_end(1, 2)
print(od)

od.move_to_end(10, last=False)
print(od)

print(od.popitem())
print(od)

print(od.pop(7))
print(od)

print(od.pop(79))
print(od)



val1 = (1,4,5)
val2 = (4,1,5)
val3 = (3, (6,7,9))
a,(b,c, d) = val3
print(a,b,c,d)

from collections import namedtuple

Point = namedtuple("Point", ['first', 'second'])
val1 = Point(7,9)
print(val1)

print(val1.first)

print(val1.second)
val1.first = 10
print(val1.first)

NestedPoints = namedtuple("nestedpoints", ['first','second'])
val1 = Point(6,9)
val2 = NestedPoints(2, val1)
print(val2)

print(val2.second.second)

# (2,9)
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
val1 = Pair(2, 9)
print(val1.first)
print(val1.second)
val1.first = 1
print(val1.first)
print(val1.second)

val2 = Pair(17, 89)
print(val2.first)
print(val2.second)
