import os

def folders(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None 
    except FileNotFoundError:
        return None, "File Not Found"
    except PermissionError:
        return None, "Permission Denied"

def main():
    folder_paths = input("Please provide the folders name with space in between folder name: ").split()

    for folder_path in folder_paths:
        files, error_message = folders(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main() 


