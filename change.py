import os

# Specify the directory where your images are located
folder_path = 'C:\\Users\\Lenovo\\Desktop\\hihi'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter and sort only image files with ".jpg" extension
image_files = sorted([f for f in files if f.lower().endswith('.txt')])

# Start renaming from index 1 (or any other starting index you prefer)
start_index = 1
for index, filename in enumerate(image_files, start=start_index):
    old_file_path = os.path.join(folder_path, filename)
    new_filename = f'AD{index:06d}.txt'  # Using :06d to format the index with leading zeros
    new_file_path = os.path.join(folder_path, new_filename)
    os.rename(old_file_path, new_file_path)
    print(f'Renamed: {filename} to {new_filename}')

print('Image files have been renamed.')
