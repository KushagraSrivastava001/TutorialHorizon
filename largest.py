def arrayConstruction(array):
    array.sort(reverse=True)
    result=0
    for i in range(len(array)):
        result=result*10+array[i]
    return int(result)
print(arrayConstruction([1,3,5,9,8]))
