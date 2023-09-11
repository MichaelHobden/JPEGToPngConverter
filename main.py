#this is programmed
import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# create folder if it doesn't exist
print(os.path.exists(f'./{output_folder}'))
if not os.path.exists(output_folder):
    os.mkdir(f'./{output_folder}')
    print("Created File")

for filename in os.listdir(f'.{image_folder}'):
    img = Image.open(f'.{image_folder}/{filename}')
    trimmed_filename = os.path.splitext(filename)[0]
    img.save(f'.{output_folder}/{trimmed_filename}.png', 'png')
