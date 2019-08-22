import os
from PIL import Image
 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    #cropped_image.show()
 
 
if __name__ == '__main__':
	i = 0

	for filename in os.listdir("/home/sam/Desktop/xxx/renamed"):
		image = '/home/sam/Desktop/xxx/renamed/Rename'+str(i)+'.png'
		crop(image, (1200, 0, 2400, 16), '/home/sam/Desktop/xxx/cropped/cropped'+str(i)+'.png')
		i += 1

