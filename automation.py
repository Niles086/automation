import os
import shutil
import glob

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")

def move_user_documents(source_folder, temporary_folder):
    try:
        shutil.move(source_folder, temporary_folder)
        print(f"User documents moved to '{temporary_folder}'.")
    except FileNotFoundError:
        print(f"User folder '{source_folder}' not found.")

def sort_documents(source_folder, destination_folder):
    create_folder(destination_folder)
    
    file_types = {
        "logs": ["*.log"],
        "mail": ["*.eml", "*.msg"],
    }

    for folder, patterns in file_types.items():
        create_folder(os.path.join(destination_folder, folder))
        for pattern in patterns:
            files = glob.glob(os.path.join(source_folder, pattern))
            for file in files:
                shutil.move(file, os.path.join(destination_folder, folder, os.path.basename(file)))
                print(f"Moved {os.path.basename(file)} to {folder} folder.")

def parse_log_file(log_file_path, target_directory):
    create_folder(target_directory)
    
    errors = []
    warnings = []

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line)

    with open(os.path.join(target_directory, 'errors.log'), 'w') as errors_file:
        errors_file.writelines(errors)

    with open(os.path.join(target_directory, 'warnings.log'), 'w') as warnings_file:
        warnings_file.writelines(warnings)

    print("Log file parsed successfully.")

def menu():
    print("Automation Menu:")
    print("1. Move user documents to temporary folder.")
    print("2. Sort documents into folders.")
    print("3. Parse log file for errors and warnings.")
    print("4. Exit.")

def execute_task(choice):
    if choice == 1:
        move_user_documents("user-docs/user", "temporary_folder")
    elif choice == 2:
        sort_documents("user-docs", "sorted_docs")
    elif choice == 3:
        parse_log_file("sorted_docs/logs/example.log", "parsed_logs")
    elif choice == 4:
        print("Exiting the application.")
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    # Initialize your project directory and structure
    create_folder("temporary_folder")
    create_folder("sorted_docs")
    create_folder("parsed_logs")

    while True:
        menu()
        user_choice = int(input("Enter your choice (1-4): "))
        execute_task(user_choice)
