import re
# Open the file in read mode
file_path = 'Day 1 /input.txt'
# Example usage with the provided lines
lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
# print("Sum of calibration values:", result)

try:
    with open(file_path, 'r') as file:
        # Read the lines from the file and create a list
        content_list = file.read().splitlines()

    # Display the created list
    print("List created from the file:")
    print(content_list)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Counter to cacluate the total sum
total_counter = 0

for i in range(len(content_list)):

    # Just extract the digits from the text
    number_extractor = re.findall(r'\d', content_list[i])

    # Since the extracted output is only numbers, extract the first and last digit seperately
    inital_digit=number_extractor[0]
    final_digit = number_extractor[-1]

    total_counter = total_counter + int(inital_digit + final_digit)

    print("Total counter:", total_counter)
    
