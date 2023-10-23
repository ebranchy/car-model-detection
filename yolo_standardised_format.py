import csv
import os

def create_txt_files(csv_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract information
            class_id = row['Class']
            x = row['x']
            y = row['y']
            w = row['w']
            h = row['h']
            image_name = row['image']

            # Prepare content for the txt file
            content = f"{class_id} {x} {y} {w} {h}"

            # Extract filename without extension
            filename_without_extension = os.path.splitext(image_name)[0]

            # Construct txt file path
            txt_file_path = os.path.join(output_folder, f"{filename_without_extension}.txt")

            # Write content to the txt file
            with open(txt_file_path, 'w') as txtfile:
                txtfile.write(content)

# Specify the path to the input CSV
input_csv_path = 'temp_lables/normalized_labels_training.csv'

# Specify the path to the output folder
output_folder_path = 'yolo_lables/cars_train'

# Create text files from CSV
create_txt_files(input_csv_path, output_folder_path)
