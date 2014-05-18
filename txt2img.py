#########################################################
#
#       PYTHON: TEXT TO IMAGE 
#
#########################################################
print 'Yay let\'s make an image!!'

# General imports
import sys
import os.path

# Import the Pillow Image Library
#   Using the Pillow image library, as the original Python
#   Image Library is no longer supported.  This is why
#   we have to specify 'from PIL' here.
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

# Global vars
FIRST_NAME = "Sue"
LAST_NAME = "Vivor"


# Create Test Image (Eventually will be PDF)
print 'Creating test image...'
imageTest = Image.new("RGB", (1700, 2200), color=0)
drawFirstName = ImageDraw.Draw(imageTest)
imageTest.save(open("imageTest.png", "wb"), "PNG")

# Dummy
print 'Creating dummy'
imageDummy = Image.new("RGBA", (100, 30))
drawDummy = ImageDraw.Draw(imageDummy)
# use a truetype font
#font = ImageFont.truetype("arial.ttf", 15)
drawDummy.text((10, 10), "HEEEEYYYY!!!!!!!!!!!!", font=None)
imageDummy.save(open("imageDummy.png", "wb"), "PNG")

# Dummy2
print 'Creating dummy2'
imageDummy2 = Image.new("RGBA", (100, 30))
drawDummy2 = ImageDraw.Draw(imageDummy2)
drawDummy2.text((10, 10), "HEEEEYYYY!!!!!!!!!!!!", font=None)
imageDummy2.save(open("imageDummy2.png", "wb"), "PNG")

# First Name
print 'Assigning first name...'
imageFirstName = Image.new("RGB", (1700, 2200))

print 'Assigning first name...'
drawFirstName = ImageDraw.Draw(imageFirstName)
drawFirstName.text((10, 10), FIRST_NAME, font=None)

print 'Assigning last name...'
drawLastName = ImageDraw.Draw(imageFirstName)
drawLastName.text((10, 50), LAST_NAME, font=None)
imageFirstName = ImageOps.invert(imageFirstName)
imageFirstName.save(open("firstName.png", "wb"), "PNG")


# Overlay First Name on Test Image
print 'Overlaying First name onto the test image'
background = Image.open("imageTest.png")
overlay = Image.open("firstName.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("combined.png","PNG")

# Overlay Last Name on Test Image
print 'Overlaying Last name onto the test image'
background = Image.open("combined.png")
overlay = Image.open("lastName.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("new.png","PNG")

