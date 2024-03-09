def filter_and_print_range(input_list, min_val, max_val):
    filtered_list = [num for num in input_list if min_val <= num <= max_val]
    output = ",".join(str(num) for num in filtered_list) + ","
    return output

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = list(map(int, user_input.split()))

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int, user_input.split())

    # Call the function to filter and print the numbers in the given range
    result = filter_and_print_range(integer_list, min_val, max_val)
    print(result)

   
