import cv2

image = cv2.imread('C:\geometrica.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#_,cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 3
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4
#cv2.drawContours(image, cnts, -1, (0,255,0), 2)

for c in cnts:
	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)
	#print(len(approx))
	x,y,w,h = cv2.boundingRect(approx)

	if len(approx)==3:
		print('Triangulo encontrado')
	else:
		print('Triangulo no encontrado')

	if len(approx)==4:
		aspect_ratio = float(w)/h
		print(aspect_ratio)
		if aspect_ratio > 1 and aspect_ratio < 1.1:
			print("Cuadrado encontrado")
		elif aspect_ratio > 1:
			print('Rectangulo horizontal encontrado')
		elif aspect_ratio < 1:
			print('Rectangulo vertical encontrado')
	else:
		print("Cuadrado no encontrado")
		print("Rectangulo no encontrado")


	if len(approx)==5:
		print('Pentagono encontrado')
	else:
		print('Pentagono no encontrado')

	if len(approx)==6:
		print('Hexagono encontrado')
	else:
		print('Hexagono no encontrado')

	if len(approx)>10:
		print('Circulo encontrado')
	else:
		print('Circulo no encontrado')
	
	cv2.drawContours(image, [approx], 0, (0,255,0),4)
	cv2.imshow('image',image)
	cv2.waitKey(0)

