# Problem 5 - Symmetric Difference
def symmetric_diff(a, b):
    result = []
    for i in a:
        if i not in b and i not in result:
            result.append(i)
    for j in b:
        if j not in a and j not in result:
            result.append(j)
    return result

print(symmetric_diff([4, 5, 2, 3, 1, 6], [8, 7, 6, 9, 4, 5]))

# Time complexity = O(n^2) , Space complexity = O(n)
