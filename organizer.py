import os
import shutil

# The folder to organize
SOURCE_DIR = "test-folder"

# The destinations
DESTINATIONS = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".txt", ".pdf", ".docx"],
    "audio": [".mp3", ".wav"]
}

def organize_files(source_path):
    # Loop through all files in the source directory
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
            
        # Get the file extension
        _, file_ext = os.path.splitext(filename)
        
        # Check if we have a rule for this extension
        moved = False
        for dir_name, extensions in DESTINATIONS.items():
            if file_ext in extensions:
                # Create the destination folder if it doesn't exist
                dest_dir_path = os.path.join(source_path, dir_name)
                os.makedirs(dest_dir_path, exist_ok=True)
                
                # Move the file
                shutil.move(file_path, dest_dir_path)
                print(f"Moved: {filename} -> {dir_name}/")
                moved = True
                break
        
        if not moved:
            print(f"Skipped: {filename}")

# --- Main part ---
if __name__ == "__main__":
    print(f"Starting organization of: {SOURCE_DIR}")
    organize_files(SOURCE_DIR)
    print("Organization complete.")
