from scipy.io import loadmat

mat = loadmat('cars_annos.mat')

type_class_names = type(mat['class_names'])
shape_class_names = mat['class_names'].shape if hasattr(mat['class_names'], 'shape') else None

class_names_row = mat['class_names'][0]

# for idx, class_name in enumerate(class_names_row):
#     print(f"Index: {idx}, Class Name: {class_name}")

# print(f"type: {type_class_names}, shape: {shape_class_names}")

first_class_name = class_names_row[0]
print(f"Shape of items in 'class_names': {first_class_name.shape}")
print(f"Content of first item: {first_class_name}")



