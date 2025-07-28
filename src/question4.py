# Problem 4 - List Intersection
def list_intersection(a, b):
    result = []
    for i in a:
        for j in b:
            if i == j and i not in result:
                result.append(i)
    return result

print(list_intersection([4, 5, 2, 3, 1, 6], [8, 7, 6, 9, 4, 5]))

# Time complexity is O(n^2) while Space complexity is O(n)
