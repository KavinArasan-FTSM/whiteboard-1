# Problem 1 - Sorting

def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Test
print(custom_sort([21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]))

# Time complexity is O(n^2) while Space is O(1).
