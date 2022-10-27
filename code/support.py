import os

# import path to each sprite and append to array
def import_sprite(path):
    sprite_list = []
    for _, __, image_files in os.walk(path):
        for image in image_files:
            full_path = path + '/' + image
            sprite_list.append(full_path)

    return sprite_list
