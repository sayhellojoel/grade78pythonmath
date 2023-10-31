import os

# Define the path to your directory
dir_path = r'G:\My Drive\Kids Schoolwork\Grade 7-8 Math + Python Series\Python Code\TXT Books All'

# Get a list of all .txt files in the directory
txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]

# Sort the file names
txt_files.sort()

# Initialize an empty string to hold the concatenated text
concatenated_text = ''

# Loop through each file
for file_name in txt_files:
    # Construct the full file path
    file_path = os.path.join(dir_path, file_name)
    
    # Open, read, and concatenate the text
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        concatenated_text += file.read() + '\n\n'  # Add an extra newline between files

# Define the path for the new concatenated file
output_path = r'G:\My Drive\Kids Schoolwork\Grade 7-8 Math + Python Series\Python Code\input.txt'

# Save the concatenated text to a new file
with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write(concatenated_text)
