import os
import re
import shutil
import argparse

# Declare regex patterns
regex_image = r'(/home/yurii/\.config/Typora/typora-user-images/[^)]+)'
pattern_image = re.compile(regex_image)

# Read cli arguments
parser = argparse.ArgumentParser(
    description="Migrates typora images from user's directory to a new directory accessed by relative path",
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument('--filename', type=str, required=True, help='A markdown file')
args = vars(parser.parse_args())
filename = args['filename']

# Create assets directory
directory = '{}.assets'.format(os.path.splitext(filename)[0])
if not os.path.exists(directory):
    os.makedirs(directory)

# Iterate over lines in the md file, copy typora image to a new directory, replace
new_lines = []
with open(filename, 'r') as file:
    for line in file:
        matches = pattern_image.finditer(line)
        new_line = line
        for match in matches:
            image_path = match.group()
            image_name = os.path.basename(image_path)
            new_image_path = os.path.join(directory, image_name)
            shutil.copyfile(image_path, new_image_path)
            print('Copying file from "{}" to "{}"'.format(image_path, new_image_path))

            new_line = re.sub(
                r'!\[[\w.-]+\]\({}\)'.format(image_path),
                '![{}]({})'.format(image_name, new_image_path),
                new_line
            )
        new_lines.append(new_line)

# Replace existent file
with open(filename, 'w') as file:
    for line in new_lines:
        file.write(line)
