import os
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from shutil import move

# Paths for dataset
dataset_path = r"D:\work\Waste Classification\waste_dataset"  # Base dataset folder
input_organic_path = os.path.join(dataset_path, "organic")
input_recyclable_path = os.path.join(dataset_path, "recyclable")
output_train_path = os.path.join(dataset_path, "train")
output_val_path = os.path.join(dataset_path, "val")
output_test_path = os.path.join(dataset_path, "test")

# Create output directories if they don't exist
for split in [output_train_path, output_val_path, output_test_path]:
    for class_name in ["organic", "recyclable"]:
        os.makedirs(os.path.join(split, class_name), exist_ok=True)

# Augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Function to augment images and move them to train, val, or test
def augment_and_distribute_images(input_path, class_name):
    # List all images in the input folder
    images = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(images)  # Shuffle for random distribution
    
    # Split images into train (70%), val (15%), and test (15%)
    train_split = int(0.7 * len(images))
    val_split = int(0.85 * len(images))
    
    train_images = images[:train_split]
    val_images = images[train_split:val_split]
    test_images = images[val_split:]
    
    # Helper function to augment and move images
    def process_images(image_list, target_path):
        for img_name in image_list:
            img_path = os.path.join(input_path, img_name)
            img = load_img(img_path)
            img_array = img_to_array(img)
            img_array = img_array.reshape((1,) + img_array.shape)
            
            # Generate and save augmented images
            save_prefix = os.path.splitext(img_name)[0]
            aug_iter = datagen.flow(img_array, batch_size=1,
                                    save_to_dir=os.path.join(target_path, class_name),
                                    save_prefix=save_prefix,
                                    save_format='jpg')
            for _ in range(5):  # Generate 5 augmented images per original image
                 next(aug_iter) 
    
    # Process and distribute images
    process_images(train_images, output_train_path)
    process_images(val_images, output_val_path)
    process_images(test_images, output_test_path)

# Augment and distribute images for both classes
augment_and_distribute_images(input_organic_path, "organic")
augment_and_distribute_images(input_recyclable_path, "recyclable")

print("Augmentation and distribution completed!")
