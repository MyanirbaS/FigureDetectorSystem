import cv2

def Define_figure(figure, w, h):
    figures = (False, False, False, False, False, False, False)
    triangulo, cuadrado, rectangulo, linea, pentagono, hexagono, circulo = figures

    if len(figure) == 3:
        print('Triangulo encontrado\n')
        triangulo = True
    elif len(figure) == 4:
        aspect_ratio = float(w)/h
        print(f'Aspec ratio: {aspect_ratio}')
        if aspect_ratio >= 0.90 and aspect_ratio < 1.1:
            print('Cuadrado encontrado\n')
            cuadrado = True
        elif aspect_ratio > 1 and aspect_ratio < 5:
            print('Rectangulo horizontal encontrado\n')
            rectangulo = True
        elif aspect_ratio < 1 and aspect_ratio > 0.1:
            print('Rectangulo vertical encontrado\n')
            rectangulo = True
        elif aspect_ratio >= 10 or aspect_ratio < 0.1:
            print('Linea encontrada\n')
            linea = True
    elif len(figure) == 5:
        print('Pentagono encontrado\n')
        pentagono = True
    elif len(figure) == 6:
        print('Hexagono encontrado\n')
        hexagono = True
    elif len(figure) > 10:
        print('Circulo Encontrado\n')
        circulo = True

def Get_contours(img):
    contours,_ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cont = 0
    Dopped_line = []

    for cnt in contours:
        cont_string = str(cont)
        cv2.drawContours(imgContours, cnt, -1, (255,0,0), 3)
        epsilon = 0.01*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(imgContours, (x,y), (x+w, y+h), (0,255,0),2)
        cv2.putText(imgContours, cont_string, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)
        area = cv2.contourArea(cnt)
        if area < 100:
            Dopped_line.append(cont)
        else:
            print(f'Figura numero: {cont_string}')
            print(f'Area: {area}')
            Define_figure(approx, w, h)
        cont+=1
    print(f'Las figuras numero: {Dopped_line} son parte de una linea punteada')

img = cv2.imread('C:\geometrica6.jpg')
imgContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgCanny = cv2.dilate(imgCanny, None, iterations=1)
imgCanny = cv2.erode(imgCanny, None, iterations=1)
Get_contours(imgCanny)

cv2.imshow('Figuras', imgContours)
cv2.waitKey(0)