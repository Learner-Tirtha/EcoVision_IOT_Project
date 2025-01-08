
import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
dataset_dir = r"D:\work\Waste Classification\waste_dataset"
output_dir = r"D:\work\Waste Classification\waste_dataset"

# Split ratios
train_ratio = 0.7
test_ratio = 0.2
val_ratio = 0.1

# Create output directories
for split in ['train', 'test', 'val']:
    for category in ['organic', 'recyclable']:
        os.makedirs(os.path.join(output_dir, split, category), exist_ok=True)

# Function to split and copy files
def split_and_copy(category):
    category_path = os.path.join(dataset_dir, category)
    files = os.listdir(category_path)
    
    # Split the data
    train_files, temp_files = train_test_split(files, test_size=(1 - train_ratio), random_state=42)
    val_files, test_files = train_test_split(temp_files, test_size=(test_ratio / (test_ratio + val_ratio)), random_state=42)
    
    # Copy files to respective folders
    for file in train_files:
        shutil.copy(os.path.join(category_path, file), os.path.join(output_dir, 'train', category))
    for file in test_files:
        shutil.copy(os.path.join(category_path, file), os.path.join(output_dir, 'test', category))
    for file in val_files:
        shutil.copy(os.path.join(category_path, file), os.path.join(output_dir, 'val', category))

# Split for each category
for category in ['organic', 'recyclable']:
    split_and_copy(category)

print("Dataset split completed!")
