
# define a function to check if two inputs are anagrams

def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False

    count = {}

    for char in string1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in string2:

        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True


print("Check to see if two words are anagrams!")

string1 = input("Enter first word: ")
string2 = input("Enter second word: ")

result = is_anagram(string1, string2)

print(result)
