import numpy as np

# Load the NumPy file
loaded_data = np.load('C:/Users/Lenovo/Downloads/MOT16-06.npy')

# Specify the path where you want to save the text file
text_file_path = 'output.txt'

# Open the text file for writing
with open(text_file_path, 'w') as text_file:
    # Iterate through the loaded NumPy array and write each element as a line in the text file
    for row in loaded_data:
        text_file.write(' '.join(map(str, row)) + '\n')

print(f'Data from the NumPy file has been converted and saved to {text_file_path}')
