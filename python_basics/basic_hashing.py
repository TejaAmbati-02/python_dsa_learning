# Highest occurring element in an array


class HighestOccurrence:
    def __init__(self, elements_array):
        self.elements_array = elements_array

    def find_highest_occurrence_element_in_an_array(self):
        max_element_cnt = 0
        max_element = 0
        num_of_elements_max_occurrence = max(self.elements_array)+ 1
        max_occurrence_array = [0] * num_of_elements_max_occurrence
        print(max_occurrence_array)
        for element in self.elements_array:
            


elements_array = [1,2,3,3,3,2]
object = HighestOccurrence(elements_array)
object.find_highest_occurrence_element_in_an_array()
