import os
import shutil
from datetime import date

# Source or root folder where files are located
source_folder = str(input(r"Enter source folder path: (e.g. C:\source) "))
# Destination/ output folder
destination_folder = str(input(r"Enter destination folder and path: (e.g. C:\output) "))
# Set initial file name
initial_name = str(input(r"Set initial file name: (e.g. document, invoice, etc.) "))

current_date = date.today()

# Create destination folder it does not exist
os.makedirs(destination_folder, exist_ok=True)

start_counter = 1

# Loop through the source_folder(where the source files are located)
for file_name in os.listdir(source_folder):
    # Check if file is in pdf format
    if file_name.endswith(".pdf"):
        source_path = os.path.join(source_folder, file_name)

        new_name = f"{initial_name}_{start_counter}_{current_date}.pdf"
        destination_path = os.path.join(destination_folder, new_name)
        
        # Use shutil.copy2 to copy also the metadata - this will copy ONLY the files from the source folder to the destination folder
        shutil.copy2(source_path, destination_path)
        start_counter += 1

# Get the total number of files renamed
total_renamed = len(os.listdir(destination_folder))

print(f"({total_renamed}) file/s renamed!")


