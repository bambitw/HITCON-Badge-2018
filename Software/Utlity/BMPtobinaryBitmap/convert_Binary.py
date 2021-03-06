import os
from PIL import Image
import numpy
import PIL.ImageOps as ImageOps
counter = 2;

bitmap_code = open('icon.c','w')

for filename in os.listdir("."):
	if ".bmp" in filename:
		print(filename)
		im = Image.open(filename)
		bitmap_code.write('const uint8_t %s []  = {'%filename.strip(".bmp"))
		width, height = im.size
		if width > 250 or height > 122:
			ratio = min(250/width, 122/height)
			im = im.resize((int(width*ratio),int(height*ratio)), Image.ANTIALIAS)
			width, height = im.size
			print("image too large, resizing %f to %dx%d" % (ratio,width, height))
			pass
		bitmap_code.write('// %d x %d \n\t'%(width,height))
		im = im.convert('L')
		im = ImageOps.invert(im)
		im = im.convert('1')
		pix = numpy.array(im)
		for x in pix:
			row_int = numpy.packbits(numpy.uint8(x)); 
			for y in  row_int:
				bitmap_code.write(str(y)+',')
				pass
			bitmap_code.write("//%d\n\t"%len(row_int))
			pass
		bitmap_code.seek(bitmap_code.tell()-1)
		bitmap_code.write("};\n")
		#print im.tobitmap(filename.strip(".bmp"))
		#bitmap_code.write(im.tobitmap(filename.strip(".bmp")).replace("char","uint8_t")+"\n")
