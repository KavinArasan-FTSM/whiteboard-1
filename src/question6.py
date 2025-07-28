# Problem 6 - Max Occurrence Character

def max_occur_char(text):
    freq = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            freq[char] = freq.get(char, 0) + 1

    if not freq:
        return None, 0  # Handle case where there are no alphabetic characters

    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

if __name__ == "__main__":   # This allows the user to enter any string and finds the character
    user_input = input("Enter a string: ")
    char, count = max_occur_char(user_input)

    if char:
        print(f"Character: '{char}', Occurrence: {count}")
    else:
        print("No alphabetic characters found in the input.")
