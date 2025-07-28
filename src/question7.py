# Problem 7 - Square Root

def square_root(x):
    if x < 0:
        raise ValueError("Input must be a non-negative integer.")
    if x == 0 or x == 1:
        return x

    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

if __name__ == "__main__":   # for desired input
    number = int(input("Enter a perfect square: "))
    result = square_root(number)
    print(f"Square root of {number} is {result}")
    
#Time Complexity: O(log x) , Space Complexity:   O(1)
