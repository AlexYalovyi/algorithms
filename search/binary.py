def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        print({ mid, guess })

        if guess == item:
            return guess
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


list = [1, 3, 5, 6, 9, 15]

print(binary_search(list, 3))