import os
import shutil
import datetime

def is_within_last_24_hours(file_path):
    twenty_four_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=24)
    file_stat = os.stat(file_path)
    modified_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)
    created_time = datetime.datetime.fromtimestamp(file_stat.st_ctime)
    return modified_time >= twenty_four_hours_ago or created_time >= twenty_four_hours_ago

def update_file(file_path):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'a') as file:
        file.write("\nUpdated at " + timestamp)

def main():
    current_directory = os.getcwd()

    # Create "last_24hours" folder if it doesn't exist
    destination_directory = os.path.join(current_directory, "last_24hours")
    os.makedirs(destination_directory, exist_ok=True)

    # Collect and update files
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        if os.path.isfile(file_path) and is_within_last_24_hours(file_path):
            update_file(file_path)
            shutil.move(file_path, destination_directory)

if __name__ == "__main__":
    main()
Updated at 2023-12-12 22:42:24