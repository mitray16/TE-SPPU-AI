def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
numbers = input("enter array (space seperated) : ").split()
numbers = [int(num) for num in numbers]
# numbers = [5, 2, 9, 1, 7]
sorted_numbers = selection_sort(numbers)
print("Sorted numbers:", sorted_numbers)
