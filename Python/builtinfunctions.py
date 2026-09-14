import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

arr = [ 1, 5, 6, 7, 4]

# sorted -> will give us a new array not inpalce
print(sorted(arr))
print(arr)

print(sorted(arr, reverse= True))
print(arr)

# sort -> will sort the array in place
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

# Absolute Sorting of the array
arr = [-1, 5, -6, 7, 4]
print(arr)
print(sorted(arr, key=lambda x: abs(x)))



fruits_list = ['apple', 'orange', 'kiwi']
print(sorted(fruits_list, key=len))
print(sorted(fruits_list, key=len, reverse=True))

arr = [5,6,8,7]
print(min(arr))
print(max(arr))
print(sum(arr))
arr1 = [-15,6,8,7]
print(max(arr1, key = lambda x: abs(x)))

fruits_list = ['Kiwi', 'Apple', 'Pineapple']
print(max(fruits_list, key= lambda x: len(x)))

print(sum(arr1))
print(sum(arr))
arr1 = [-15,6,8,7]
print(sum(arr1))