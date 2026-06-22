import heapq

val = []

heapq.heappush(val, 10)
heapq.heappush(val, 7)

heapq.heappush(val, 9)
print(val)

heapq.heappush(val, 19)
print(val)

heapq.heappush(val, 12)
print(val)

heapq.heappush(val, 1)
print(val)

heapq.heappop(val) # Smallest element is taken out
print(val)

heapq.heappushpop(val, 9) # 1st Push 9 and then pop the smallest element
print(val)

heapq.heapreplace(val, 29) # 1st pop the smallest element and then Push 29
print(val)

heapq.heapreplace(val, 1) # 1st pop the smallest element and then Push 1
print(val)


print(heapq.nlargest(3, [7,1,5,3,10])) # Get 3 largest elements

print(heapq.nsmallest(3, [7,1,5,3,10])) # Get 3 smallest elements

arr = [ 7, 8, 2, 1, -16, 6]

for item in arr:
    heapq.heappush(arr, item)

heapq.heapify(arr)
print(arr)

arr = [ 6, 7, 8, 9, 10]
pq = []
for item in arr:
    heapq.heappush(pq, -1 * item)
print(-1 * pq[0])

import bisect

arr = [4,5,6,7,7,9,10,12,12,13]
print(bisect.bisect_left(arr, 5)) ## Where can we insert the value, so the order is maintained assuming array is sorted
print(bisect.bisect_left(arr, 1))
print(bisect.bisect_left(arr, 11))

print(bisect.bisect_right(arr, 5)) ## Where can we insert the value, so the order is maintained assuming array is sorted
print(bisect.bisect_right(arr, 1))
print(bisect.bisect_right(arr, 11))

print(bisect.bisect(arr, 5)) ## Where can we insert the value, so the order is maintained assuming array is sorted
print(bisect.bisect(arr, 1))
print(bisect.bisect(arr, 11))

print(arr)

bisect.insort(arr, 5)
print(arr)

bisect.insort_left(arr, 8)
print(arr)

bisect.insort_right(arr, 1)
print(arr)


import itertools

arr = [1,5,6,7]

print(list(itertools.combinations(arr, 2))) # all 2 length unique combinations

print(list(itertools.combinations(arr, 3))) # all 3 length unique combinations


print(list(itertools.combinations_with_replacement(arr, 2))) # all 2 length combinations including duplicates , consider itself

print(list(itertools.combinations_with_replacement(arr, 3))) # all 3 length combinations including duplicates , consider itself

print(list(itertools.permutations(arr, 3))) # Permutations -> (a,b) and (b,a) as well

arr1 = [1,2]
arr2 = [3,4]

print(list(itertools.product(arr1, arr2)))

arr1 = [1,2]
arr2 = [3,4]
arr3 = [5,6]
print(list(itertools.product(arr1, arr2, arr3))) # All combinations 

arr = [1,2,3,4]
list(itertools.cycle(arr)) # Repeat items indefinitely

print(list(itertools.repeat(5, 6))) # Repeat the given items in given number of  times

print(list(itertools.chain([1, 2],[5,6],[3,4]))) # Repeat the given items in given number of  times

arr = [1,3,6,10]
print(list(itertools.accumulate(arr))) # Returns acculator sum still that element in the array (Running Total)

print(list(itertools.accumulate(arr, lambda x, y : x* y))) # Returns acculator given lambda operation  still that element in the array (Running operation)


import math
print(math.pi)
print(math.e)
print(math.pow(2,3))
print(math.pow(2,-3))
print(math.sqrt(16))
print(math.factorial(5))
print(math.gcd(10, 15))
print(math.lcm(10, 15))
print(math.log(89))
print(math.log10(89))
print(math.log2(89))
print(math.sin(89))
print(math.cos(89))
print(math.degrees(89))
print(math.radians(89))
print(math.ceil(89.345))
print(math.floor(89.345))
print(math.isfinite(float('inf')))
print(math.isinf(float('inf')))



import random

print(random.random())
print(random.randint(1, 100))
print(random.randrange(0, 100, 2))
print(random.choice([1,5,6,7]))
print(random.sample([1,5,6,7], 2))

arr = [1,5,6,7]
random.shuffle(arr)
print(arr)

print(random.uniform(1.0, 10.0))


arr = [1,6,2,4]
arr.append(7)
print(arr)
arr.extend([1,4])
arr.insert(1,10)
print(arr)
arr.remove(6)
print(arr)
print(arr.pop())
print(arr)

arr.pop(2)
print(arr)

print(arr.index(7))

print(arr.count(1))

arr.sort()
print(arr)

# arr.reverse()
# print(arr)

arr.sort(reverse=True)
print(arr)

arr2 = arr.copy() # Shallow Copy
print(arr2)

arr.clear()
print(arr)
print(arr2)



dd = {1:'teja',2:"sai", 79:"kumar"}
dd[100] = 'century'
print(dd)
dd.update({10:"messi"})
print(dd)
print(dd.get(10))
print(dd[100])
print(dd.get(109, 'Not Found'))
print(dd.pop(10))
print(dd.popitem())
print(dd)
arr = list(dd.keys())
print(arr)
arr = list(dd.values())
print(arr)
arr = list(dd.items())
print(arr)

for key, value in dd.items():
    print(key, value)

dd.clear()
print(dd)


st = {1, 4, 5, 6, 3,  1}
print(st)

st.add(0)
print(st)

st.remove(5)
print(st)

# st.remove(15)
# print(st)

if 15 in st:
    st.remove(15)
else:
    print("Not Present")

st.discard(5)
print(st)

st.discard(15)
print(st)

print(st.pop())
print(st)

st1 = st.copy()
print(st1)

print(st.clear())

print(st)



st = "teja"

print(st.upper())

print(st.lower())

print(st.capitalize())

print(st.title())

st = "                teja                    "
print(st.strip(" "))

st = "Teja Sai Kumar"
print(st.split(" "))

print("|".join(st.split(" ")))

print(st.replace("Sai", "Ambati"))
