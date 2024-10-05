def remove_duplicates(sorted_array):
    # Initialize an empty list to store the result
    result = []
    
    # Loop through the sorted array
    for i in range(len(sorted_array)):
        # If the result is empty or the current element is not equal to the last one added to the result
        if len(result) == 0 or sorted_array[i] != result[-1]:
            result.append(sorted_array[i])  # Add the current element to the result
    
    return result
array=[1,2,3,3,5,5,6,6,6,6,7,8,8,9]
print(remove_duplicates(array))