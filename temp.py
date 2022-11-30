import pytesseract
import cv2
import os,sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def read_from_img(img,oem,psm):
	with open(resource_path(r'images/tesseract.txt'), 'r') as f:
		tesse_location = f.readline()
	processed_text = "cadena vacia"
	#wait for branch merging then try to adjust screenshot area to allow tesseract to read accurately
	#check if program is installed
	file_exists2 = os.path.exists(tesse_location)
	if file_exists2 == False:
		#there's not Tesseract Installed
		print("No encontré Tesseract")
		return
	
	# read image
	image = cv2.imread(img)
	# configurations
	#config = ('-l kor --oem 1 --psm 7')
	config = (f'-l kor --oem {oem} --psm {psm}')
	# pytessercat
	pytesseract.pytesseract.tesseract_cmd = tesse_location
	try:
		text = pytesseract.image_to_string(image, config=config)
	except:
		print(f"No se pudo con {oem,psm}")
		return
	# print text
	text = text.split('\n')
	print(text)
"""	for letter in text:
	#check for nonexistant HU
		if len(letter)<3:
			continue
		elif "no existe" in letter or "ya esta eliminada" in letter:
			processed_text = "HU no existente"
		else:
			processed_text = f"El error tenía esto {letter}, pero no pude detectar caracteres"

	return processed_text
"""
oem = 1
psm = 1

for x in range(39):
	read_from_img(r'C:\Users\L14\Documents\Korean_OCR\Kormulti.jpg',oem,psm)
	oem +=1
	print(oem,psm)
	if oem >3:
		oem = 0
		psm +=1
	