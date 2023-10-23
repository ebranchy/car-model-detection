import csv
from PIL import Image
import os

def normalize_coordinates(row, width, height):
    # Convert str to int
    x1, y1, x2, y2 = map(int, [row['x1'], row['y1'], row['x2'], row['y2']])

    # Calculate width and height of the box
    box_width = x2 - x1
    box_height = y2 - y1

    # Calculate center of the box
    center_x = x1 + box_width / 2
    center_y = y1 + box_height / 2

    # Normalize the coordinates
    norm_center_x = center_x / width
    norm_center_y = center_y / height
    norm_width = box_width / width
    norm_height = box_height / height

    return norm_center_x, norm_center_y, norm_width, norm_height

def process_images(csv_input_path, images_folder, csv_output_path):
    with open(csv_input_path, newline='') as csvfile, \
         open(csv_output_path, 'w', newline='') as write_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['Class', 'image', 'x', 'y', 'w', 'h']  # specify the headers of the new csv
        writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            image_name = row['image']
            image_path = os.path.join(images_folder, image_name)
            
            try:
                with Image.open(image_path) as img:
                    width, height = img.size

                norm_x, norm_y, norm_w, norm_h = normalize_coordinates(row, width, height)

                # Write normalized coordinates to new csv
                writer.writerow({'Class': row['Class'], 'image': image_name, 'x': norm_x, 'y': norm_y, 'w': norm_w, 'h': norm_h})
            except Exception as e:
                print(f"Error processing image {image_name}: {str(e)}")

# Update these paths as necessary
csv_input_path = 'source_lables/cardatasettrain.csv'
images_folder = 'stanford-cars-dataset/images/cars_train'
csv_output_path = 'temp_lables/normalized_labels_training.csv'

process_images(csv_input_path, images_folder, csv_output_path)


