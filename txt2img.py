#########################################################
#
#       PYTHON: TEXT TO IMAGE 
#
#########################################################
print 'Yay let\'s make an image!!\n'

# General imports
import sys
import os.path

# GSpread for manipulating Google Docs with Python
import gspread

# Import the Pillow Image Library
#   Using the Pillow image library, as the original Python
#   Image Library is no longer supported.  This is why
#   we have to specify 'from PIL' here.
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

# Global vars for now..
FIRST_NAME = ""
LAST_NAME = ""
DATE = ""
STREET = ""
CITY = ""
STATE = ""
ZIP = ""
PHONE = ""
EMAIL = ""

# I know I should never do it like this. But it is a hackathon
# DOCS_EMAIL = ""
# DOCS_PASSWORD = ""
DOCS_EMAIL = "user02@team01.govchal00.com"
DOCS_PASSWORD = "GovSafe02"

def makeTransparent():
	img = Image.open('imageTemporary.png')
	imga = img.convert("RGBA")
	datas = imga.getdata()

	newData = list()
	for item in datas:
	    if item[0] == 255 and item[1] == 255 and item[2] == 255:
	        newData.append([255, 255, 255, 0])
	    else:
	        newData.append(item)

	imgb = Image.frombuffer("RGBA", imga.size, newData, "raw", "RGBA", 0, 1)
	# imgb.save(open("imageTestA.png", "wb"), "PNG")

def initDataFromGDocs():
	print 'Fetching data from Google Docs...'

	global FIRST_NAME
	global LAST_NAME
	global DATE
	global STREET
	global CITY
	global STATE
	global ZIP
	global PHONE
	global EMAIL

	# Login with your Google account
	# I know I should NEVER do this like this. But this is a hackathon...
	gc = gspread.login(DOCS_EMAIL, DOCS_PASSWORD)

	# Open a worksheet from spreadsheet with one shot
	wks = gc.open("GovSafeData").sheet1

	# Populate 
	FIRST_NAME = wks.acell('A2').value
	LAST_NAME = wks.acell('B2').value
	DATE = wks.acell('C2').value
	STREET = wks.acell('D2').value
	CITY = wks.acell('E2').value
	STATE = wks.acell('F2').value
	ZIP = wks.acell('G2').value
	PHONE = wks.acell('H2').value
	EMAIL = wks.acell('I2').value

def DrawData01():
	print '\nCreating temporary image for DAC...'
	imageTemporary = Image.new("RGB", (1275,1650))

	#print 'Assigning first name...'
	drawFirstName = ImageDraw.Draw(imageTemporary)
	drawFirstName.text((360, 183), FIRST_NAME, font=None)

	#print 'Assigning last name...'
	drawLastName = ImageDraw.Draw(imageTemporary)
	drawLastName.text((540, 183), LAST_NAME, font=None)

	#print 'Assigning date...'
	drawDate = ImageDraw.Draw(imageTemporary)
	drawDate.text((935, 183), DATE, font=None)

	address = STREET + ', ' + CITY + ', ' + STATE + ' ' + ZIP
	#print 'Assigning address 1...'
	drawAddress1 = ImageDraw.Draw(imageTemporary)
	drawAddress1.text((540, 230), address, font=None)

	#print 'Assigning address 2...'
	drawAddress2 = ImageDraw.Draw(imageTemporary)
	drawAddress2.text((405, 327), address, font=None)

	#print 'Assigning email address...'
	drawAddress = ImageDraw.Draw(imageTemporary)
	drawAddress.text((340, 380), EMAIL, font=None)

	#print 'Assigning phone number...'
	drawPhone = ImageDraw.Draw(imageTemporary)
	drawPhone.text((370, 530), PHONE, font=None)

	print 'Saving temporary image...'
	imageTemporary = ImageOps.invert(imageTemporary)
	imageTemporary.save(open("imageTemporary.png", "wb"), "PNG")

def overlayAndSave01():
	print 'Overlaying dataset on form...\n'

	background = Image.open("originals/DACintakeform-Draft.png")
	overlay = Image.open("imageTemporary.png")

	background = background.convert("RGBA")
	overlay = overlay.convert("RGBA")

	new_img = Image.blend(background, overlay, 0.5)
	new_img = new_img.convert("RGB")
	#new_img.save("DAC_edited.pdf","PDF", resolution=100.0)
	filename = "finals/DACintakeform-Draft" + LAST_NAME + FIRST_NAME + ".png"
	new_img.save(filename,"PNG")

def DrawData02():
	print '\nCreating temporary image for DAC...'
	imageTemporary2 = Image.new("RGB", (1275,1650))

	#print 'Assigning first name...'
	drawFirstName2 = ImageDraw.Draw(imageTemporary2)
	drawFirstName2.text((420, 345), FIRST_NAME, font=None)

	#print 'Assigning last name...'
	drawLastName2 = ImageDraw.Draw(imageTemporary2)
	drawLastName2.text((450, 345), LAST_NAME, font=None)

	#print 'Assigning date...'
	drawDate2 = ImageDraw.Draw(imageTemporary2)
	drawDate2.text((360, 295), DATE, font=None)

	address = STREET + ', ' + CITY + ', ' + STATE + ' ' + ZIP
	#print 'Assigning address 1...'
	drawAddress12 = ImageDraw.Draw(imageTemporary2)
	drawAddress12.text((420, 365), address, font=None)

	#print 'Assigning address 2...'
	drawAddress22 = ImageDraw.Draw(imageTemporary2)
	drawAddress22.text((420, 395), address, font=None)

	#print 'Assigning email address...'
	drawAddress2 = ImageDraw.Draw(imageTemporary2)
	drawAddress2.text((420, 495), EMAIL, font=None)

	#print 'Assigning phone number...'
	drawPhone2 = ImageDraw.Draw(imageTemporary2)
	drawPhone2.text((370, 560), PHONE, font=None)

	print 'Saving temporary image...'
	imageTemporary2 = ImageOps.invert(imageTemporary2)
	imageTemporary2.save(open("imageTemporary2.png", "wb"), "PNG")

def overlayAndSave02():
	print 'Overlaying dataset on form...\n'

	background = Image.open("originals/Waldo_Canyon_DAC_Intake.png")
	overlay = Image.open("imageTemporary2.png")

	background = background.convert("RGBA")
	overlay = overlay.convert("RGBA")

	new_img = Image.blend(background, overlay, 0.5)
	new_img = new_img.convert("RGB")
	#new_img.save("DAC_edited.pdf","PDF", resolution=100.0)
	filename = "finals/Waldo_Canyon_DAC_Intake" + LAST_NAME + '_' + FIRST_NAME + ".png"
	new_img.save(filename,"PNG")

initDataFromGDocs()

DrawData01()
overlayAndSave01()

DrawData02()
overlayAndSave02()







