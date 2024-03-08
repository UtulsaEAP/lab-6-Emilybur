def check_palindrome(user_input):
    # Remove spaces from input
    #Emily Burke Lab Friday at 3
    user_input = user_input.replace(" ", "")
    
    # Check if the input is equal to its reverse
    if user_input == user_input[::-1]:
        print(f"palindrome: {user_input}")
    else:
        print(f"not a palindrome: {user_input}")

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)

