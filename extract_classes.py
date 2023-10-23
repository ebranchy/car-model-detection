from scipy.io import loadmat
import csv

mat = loadmat('cars_annos.mat')

class_names = mat['class_names']

class_names_list = class_names[0]  # get the list of class names

# Extract the actual strings if they're wrapped in another array
# This is necessary because it appears each element in 'class_names' is itself a 1-element array
class_names_list = [item[0] for item in class_names_list]

with open('classes.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Writing class names to the CSV file
    for index, class_name in enumerate(class_names_list):
        writer.writerow([f"{index}: {class_name}"])