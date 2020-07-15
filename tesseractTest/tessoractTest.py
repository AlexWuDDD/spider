import tesserocr
from PIL import Image
image = Image.open('../capture/tesserocrTest.jpg')
print(tesserocr.image_to_text(image))

print(tesserocr.file_to_text('../capture/tesserocrTest.jpg'))
