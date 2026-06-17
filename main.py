import os
import shutil

# folderul de test
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, "test_files")

# categorii
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"] 
}

def get_category(file_name):
    _, ext = os.path.splitext(file_name)
    
    for category, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            return category
    
    return "Others"


def organize_files():
    if not os.path.exists(SOURCE_DIR):
        print("Folder not found!")
        return

    for file in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, file)

        if os.path.isfile(file_path):
            category = get_category(file)

            category_path = os.path.join(SOURCE_DIR, category)
            os.makedirs(category_path, exist_ok=True)

            shutil.move(file_path, os.path.join(category_path, file))

            print(f"Moved {file} -> {category}/")


if __name__ == "__main__":
    organize_files()