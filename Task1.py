# Importing Libraries
import os
import shutil
import datetime
import pandas as pd

# Function for reading the images from the folders and sub-folders
def reading_images(folder_path):

    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)

        if not os.path.exists(destination_folder): # Create the destination folder if it doesn't exist
            os.makedirs(destination_folder)

        if os.path.isdir(file_path): # check if the item is directory or not
            reading_images(file_path)
        else:
            with open(file_path, 'r') as file:
                # extracting the name
                image_title = os.path.basename(file_path)
                extracted_title = image_title.split('-')[-1]
                images_names.append(extracted_title)

                # extracting the size
                image_size_bytes = os.path.getsize(file_path)
                image_size_mb = str(round(image_size_bytes / (1024 * 1024), 2)) + " MB"  # 1 MB = 1024 * 1024 bytes
                images_sizes.append(image_size_mb)

                # extracting the modification time
                timestamp = os.path.getmtime(file_path)
                modification_date = datetime.datetime.fromtimestamp(timestamp)
                formatted_datetime = modification_date.strftime("%A %b %d %H:%M:%S %Y")
                modification_dates.append(formatted_datetime)

                # converting the extracted information into csv file
                data = {'Image': images_names, 'Image Size': images_sizes, 'Image Modification date': modification_dates}
                data = pd.DataFrame(data)
                data.to_csv('data.csv', index=False)

                # copying all images into one folder
                shutil.copy(file_path, destination_folder)

# Source and destination folders containing the images
source_folder = 'D:\\eT3 challenge\\dairies'
destination_folder = 'D:\\eT3 challenge\\images dataset for ex.'

images_sizes = []
images_names = []
modification_dates = []
# calling the function
reading_images(source_folder)
