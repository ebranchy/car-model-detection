import csv
import os

def check_and_reindex_class(csv_path):
    rows = []
    class_zero_exists = False
    archive_file_path = os.path.splitext(csv_path)[0] + "_archived.csv"

    # Read the existing CSV and check if there's a 'Class' value of 0
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Class'] == '0':
                class_zero_exists = True
            rows.append(row)

    # If there's no 'Class' value of 0, reindex the 'Class' values and write to the file
    if not class_zero_exists:
        for row in rows:
            row['Class'] = str(int(row['Class']) - 1)

        # Rename the original file for archiving
        os.rename(csv_path, archive_file_path)

        # Write the updated data back to the original file
        with open(csv_path, 'w', newline='') as csvfile:
            fieldnames = ['Class', 'image', 'x', 'y', 'w', 'h']  # specify the headers of the csv
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        return True  # Reindexing occurred

    return False  # No reindexing was necessary

# Specify the path to the input CSV
input_csv_path = 'temp_lables/normalized_labels_training.csv'

# Check and reindex if necessary
reindexed = check_and_reindex_class(input_csv_path)

if reindexed:
    print("The 'Class' values were reindexed, and the original file was archived.")
else:
    print("A 'Class' value of 0 already exists. No reindexing or file changes were necessary.")