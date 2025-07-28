#question 8 - Anagram
def clean_text(text):
    return ''.join(char.lower() for char in text if char.isalpha())

def are_anagrams(str1, str2):
    cleaned_str1 = clean_text(str1)
    cleaned_str2 = clean_text(str2)
    return sorted(cleaned_str1) == sorted(cleaned_str2)

if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    result = are_anagrams(s1, s2)
    print("Result:", result)

#time complexity is O(n log n + m log m) while space complexity is O(n + m)
