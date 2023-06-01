def selectionSort(arr):
    newArr = []

    for i in range(0, len(arr)):
        smallest_index = 0
        for j in range(0, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        newArr.append(arr.pop(smallest_index))
        print(newArr)
    
    return newArr

arr = [3, 1, 5, 6, 2, 10, 4]

print(selectionSort(arr))
