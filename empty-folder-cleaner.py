import os


def list_empty_folders(root_dir):
    return [dirpath for dirpath, dirnames, filenames in os.walk(root_dir) if not dirnames and not filenames]


def delete_folders(folders, indices_to_delete=None):
    try:
        for folder in folders if not indices_to_delete else (folders[index] for index in indices_to_delete):
            confirmation = input(f"Delete '{folder}'? (y/n): ").lower()
            if confirmation == 'y':
                os.rmdir(folder)
                print(f"Deleted: {folder}")
            else:
                print(f"Cancelled deletion of '{folder}'.")
    except OSError as e:
        print(f"Error deleting folder: {e}")


def main():
    while True:
        target_directory = input("Enter directory path: ")
        empty_folders = list_empty_folders(target_directory)

        if not empty_folders:
            print("No empty folders found.")
            continue

        print("Empty folders:")
        for i, folder in enumerate(empty_folders, 1):
            print(f"{i}. {folder}")

        choice = input("Delete these folders? (y/n/s): ").lower()

        if choice == 'y':
            confirmation = input("Delete ALL empty folders? (y/n): ").lower()
            if confirmation == 'y':
                delete_folders(empty_folders)
                print("Folders deleted successfully.")
            else:
                print("Deletion cancelled.")
        elif choice == 's':
            try:
                indices_to_delete = [int(idx.strip()) - 1 for idx in input("Enter folder numbers (comma-separated): ").split(",")]
                confirmation = input(f"Delete selected folders? (y/n): ").lower()
                if confirmation == 'y':
                    delete_folders(empty_folders, indices_to_delete)
                    print("Selected folders deleted successfully.")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Invalid input. Please enter valid folder numbers.")
        else:
            print("Folders were not deleted.")

        continue_processing = input("Process another directory? (y/n): ").lower()
        if continue_processing != 'y':
            break


if __name__ == "__main__":
    main()
