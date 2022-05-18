import pandas as pd
import os
import shutil

"""
- This code will filter images by vendor . 
- will read Excel sheet , read image name , vendor for this image
- look for the image file , read its name , look who is the vendor , make directory for it , if not have one
- if have a directory read the image name , grap the vendor and move the image from current path to new folder
 for the vendor who belong.

"""

def read_excel(path_to_file):
    df = pd.read_excel(path_to_file)
    return df


def dataframe_to_dict(df, key_column, value_column):
    p_id_v_id = df.set_index(key_column)[value_column].to_dict()
    return p_id_v_id


def move_images(dataframe_to_dict, source):
    data = dataframe_to_dict
    dir = source
    files = os.listdir(image_folder)  # grab image folder
    repeted=['(1)', '(2)']
    for file in files:
        image_without_png = file.rsplit('.', 1)[0]
        vendor_for_this_image = data.get(int(image_without_png))
        if vendor_for_this_image:
            dir_path = f'D:\\image filtration\\New_filtered_folder\\{vendor_for_this_image}'
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            if os.path.exists(dir_path):
                file_path = f'{dir}\\{file}'


            if int(image_without_png) in data:
                try:
                    new_path = shutil.move(f"{source}/{file}", dir_path)
                except OSError:
                    os.remove(f"{source}/{file}")


            else:
                continue

        else:
            continue


if __name__ == "__main__":
    path_to_file = 'D:\image filtration\ids.xlsx'
    image_folder = source = 'D:\Rejected from Smadi'
    df = read_excel(path_to_file)

    p_id_v_id = dataframe_to_dict(df, 'product_id', 'entityId')
    print(p_id_v_id)
    move_images(p_id_v_id, source)
