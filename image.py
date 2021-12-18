import sys
import os
from PIL import Image

def jpgtopng_converter():

	image_folder = sys.argv[1]
	output_folder = sys.argv[2]

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	for filename in os.listdir(image_folder):
		img = Image.open(f'{image_folder}{filename}')
		clean_name = os.path.splitext(filename)[0]
		img.save(f'{output_folder}{clean_name}.png','png')
		print('all done')

def gray_image():

	image_folder = sys.argv[1]
	output_folder = sys.argv[2]

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	for filename in os.listdir(image_folder):
		img = Image.open(f'{image_folder}{filename}')
		filtered_img = img.convert("L")
		filtered_img.save(f'{output_folder}{filename}')
		print('all done!')


def thumbnail():
	image_folder = sys.argv[1]
	output_folder = sys.argv[2]
	size = (400,400)

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
		
	for filename in os.listdir(image_folder):
		img = Image.open(f'{image_folder}{filename}')
		img.thumbnail(size)
		img.save(f'{output_folder}{filename}')
		print('all done!')


thumbnail()