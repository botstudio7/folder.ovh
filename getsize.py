import os
import csv

def calculate_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def main():
    # Prompt user for folder path
    print("Script powered by folder.ovh")
    folder_path = input("Enter the folder path: ")

    # Ensure the folder path ends with a backslash
    if not folder_path.endswith(os.path.sep):
        folder_path += os.path.sep

    # Set the output CSV file path
    output_file = "FolderSizeReport.csv"

    # Open CSV file for writing
    with open(output_file, mode='w', newline='') as csv_file:
        # Create CSV writer
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write header row
        #csv_writer.writerow(['Item Name', 'Total Size (Bytes)'])

        # Iterate through each folder and file
        for item_name in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item_name)
            size = calculate_folder_size(item_path) if os.path.isdir(item_path) else os.path.getsize(item_path)

            # Append data to CSV file
            csv_writer.writerow([item_name, size])

            # Display progress
            print(f"Calculating... {item_path}")

    # Notify user that the process is complete
    print(f"Calculation completed. Results saved to {output_file}")

if __name__ == "__main__":
    main()
