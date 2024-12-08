import os
import json
import tags


def get_folder_names(directory):
    folder_names = []
    try:
        for item in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, item)):
                folder_names.append(item)
    except Exception as e:
        print(f"An error occurred: {e}")
    return folder_names






directory = "C:/Users/james/OneDrive/Documents/GitHub/Individual-Project/cad2/task1/audio/musdb18_hq/train/audios"

# Get the list of folder names
folder_names = get_folder_names(directory)

# Print the list of folder names
print(folder_names)

feature_list  = {}


# Music descriptors go here



# Find shared tags
# shared_tags = songs["song1"].intersection(songs["song2"])


