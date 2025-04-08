def file_to_array_with_limit(file_path, char_limit):

    """
    OK.  I BORROWED THIS WHOLE CLOTH.   Reads a text file into an array, limiting the number of characters per element.

    Args:
        file_path (str): The path to the text file.
        char_limit (int): The maximum number of characters per element.

    Returns:
        list: An array of strings, with each string having at most char_limit characters.
              Returns an empty list if the file is not found or an error occurs.
    """
    try:
        with open('turing.txt', 'r') as file:
            lines = file.readlines()

            result_array = []
            for line in lines:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Avoid adding empty strings
                    result_array.extend([line[i:i + char_limit] for i in range(0, len(line), char_limit)])
                    # print(result_array, 'RESULT ARRAY')
            return result_array
    except FileNotFoundError:
        print(f"Error: File not found at path: {'turing.txt'}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
file_path = 'turing.txt'  # Replace with the actual file path
char_limit = 76
array_result = file_to_array_with_limit(file_path, char_limit)
Count = 0
if array_result:
    print("Array elements:")
    for element in array_result:
        print(f"'{element}'")

    for line in array_result:
        Count+=1
    print (Count)
    # print(array_result[1])
    print(array_result[5])
    print(array_result[6])
    print(array_result[7])



else:
    print("No data was read into the array.")
