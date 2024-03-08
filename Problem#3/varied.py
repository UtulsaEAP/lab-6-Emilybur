def process_input(input_string):
    # Split into separate strings
    #Emily Burke Lab Friday at 3
    numbers = input_string.split()

    # Convert strings to floats
    numbers = [float(num) for num in numbers]

    # Get max and average
    max_value = max(numbers)
    average_value = sum(numbers) / len(numbers)
    return max_value, average_value

if __name__ == "__main__":
    
    # Call the function and get the results
    user_input=input()
    max_value, average_value = process_input(user_input)

    print(f'{max_value:.2f}, {average_value:.2f}')
    

