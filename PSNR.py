import numpy as np
import math
import cv2

def Representational(r,g,b):
	return (0.299*r+0.287*g+0.114*b)

def main():
	
	#Loading images (orignal image and compressed image)
	orignal_image = cv2.imread('orignal_image.png',1)
	compressed_image = cv2.imread('compressed_image.png',1)

	#Getting image height and width
	height,width = orignal_image.shape[:2]

	#Error
	error_sum = 0.0

	#
	orignalPixelAt = 0.0
	compressedPixelAt = 0.0

	for i in range(height):
		for j in range(width):
			orignalPixelAt =Representational(orignal_image[i][j][0],orignal_image[i][j][1],orignal_image[i][j][2])
			compressedPixelAt = Representational(compressed_image[i][j][0],compressed_image[i][j][1],compressed_image[i][j][2])
			diff = pow(abs(orignalPixelAt-compressedPixelAt),2)
			error_sum = error_sum + diff

	MSR = error_sum/(height*width)
	PSNR = -(10*math.log10(MSR/(255*255)))

	print "PSNR value is " +str(int(PSNR))


if __name__ == '__main__':
	main()

