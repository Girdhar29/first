# Write a Python script to:
#     - Accept a string input from the user and check if it's a palindrome.
#     - Count the frequency of each character in the string.


def palindrome(s):  #define function
                                                                  
    normalized_str = ''.join(s.split()).lower()    #normalize input like removing space and converting lowercse
    return normalized_str == normalized_str[::-1]  #check the input is same as in reverse

def char_freq(s):
    frequency = {}
    for char in s:
        if char.isalnum():                 # Consider only alphanumeric characters
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

def main():
    user_input = input("Enter any string: ")   # user input
    
    
    if palindrome(user_input):   # Check the input string is a palindrome or not
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')
    
  
    freq = char_freq(user_input)     # Count the frequency of each character in the string
    print("Character frequency:")
    for char, count in freq.items():
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()