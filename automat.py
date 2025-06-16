import os
import shutil

# Define source (Downloads folder) and destination folders
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")
DESTINATIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'PDFs': ['.pdf'],
    'ZIPs': ['.zip', '.rar'],
    'Docs': ['.docx', '.doc', '.txt']
}

# Function to organize files
def organize_downloads():
    for file_name in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, file_name)
        
        if os.path.isfile(file_path):
            ext = os.path.splitext(file_name)[1].lower()
            for folder, extensions in DESTINATIONS.items():
                if ext in extensions:
                    dest_folder = os.path.join(DOWNLOADS_DIR, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file_name))
                    print(f"Moved: {file_name} → {folder}/")
                    break

# Run the script
organize_downloads()
