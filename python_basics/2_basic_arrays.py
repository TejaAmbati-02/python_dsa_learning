class BasicArrays:
    def __init__(self, arr):
        self.arr = arr

    def sum_of_array_elements(self):
        self.sum_of_arrays = 0
        for i in range(0, len(self.arr)):
            # print(self.arr[i])
            self.sum_of_arrays += self.arr[i]
        return self.sum_of_arrays


    def count_odd_numbers(self):
        self.odd_numbers_count = 0
        for i in range(0, len(self.arr)):
            # print(self.arr[i])
            if self.arr[i] % 2 != 0:
                self.odd_numbers_count += 1
        return self.odd_numbers_count

    def check_array_is_sorted(self):
        if len(self.arr) <=1: return True
        else:
            for i in range(1, len(self.arr)):
                if self.arr[i-1] > self.arr[i]:
                    return False
            return True

    def reverse_array(self):
        start = 0
        end = len(self.arr) - 1
        while start < end:
            self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
            start += 1
            end -= 1
        return self.arr



basic_arrays = BasicArrays([1, 2, 3, 4, 5, 1])
print(basic_arrays.sum_of_array_elements())
print("=============================")
print(basic_arrays.count_odd_numbers())
print("=============================")
print(basic_arrays.check_array_is_sorted())
print("=============================")
print(basic_arrays.reverse_array())
print("=============================")