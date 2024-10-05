def remove_duplicates(sorted_array):
    result = []

    for i in range(len(sorted_array)):
        if len(result) == 0 or sorted_array[i] != result[-1]:
            result.append(sorted_array[i])
    
    return result
array=[2,3,4,4,6,7,7]
print(remove_duplicates(array))
