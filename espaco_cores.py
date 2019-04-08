import cv2
import math as m
import numpy as np 

def main():

    img = cv2.imread('helena.jpg')

    #tamanho da mascara
    w_size = 5

    cv2.imshow('Imagem Original', img)
    #cv2.imshow('Imagem CMY', convertCMY(img))
    #cv2.imshow('Imagem HSI', convertHSI(img))
    #convertHSI(img)

    #cv2.imshow('Mediana RGB',mediana_RGB(img, w_size))
    #cv2.imshow('Mediana CMY',mediana_CMY(convertCMY(img), w_size))
    cv2.imshow('Mediana HSI',mediana_HSI(convertHSI(img), w_size))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##################################################################################
#           Converte imagem RGB para CMY
def convertCMY(f):
    g = np.copy(f)
    g = 1-g 
    return g
##################################################################################
#           converte imagem RGB para HSI

#           resolver problema...

def convertHSI(f):
    size = f.shape
    img = np.zeros(size).astype(float)
    H = 0
    for i in range(size[0]-1):
        for j in range(size[1]-1):
            
            r = f[i][j][2]
            g = f[i][j][1]
            b = f[i][j][0]


            aux = (r+g+b)

            minimo = min(r,g,b)
            
            I = aux/3
            S = 1 - 3*(minimo/(aux))

            if(S < 0.0001):
                S = 0
            elif(S > 0.9999):
                S = 1

            if(S != 0):
                H = (0.5*((r-g)+(r-b)/m.sqrt( m.pow((r-g),2)+((r-b)*(g-b)))))
                
                if(b<=g):
                    H=H
                else:
                    H = (((360*m.pi)/180.0) - H)
            
            img[i][j][0] = (H*180)/m.pi
            img[i][j][1] = S*100
            img[i][j][2] = I
    return img

####################################################################################
#           mediana com imagem RGB...
def mediana_RGB(f,w_size):

    size = f.shape

    g = np.zeros((size[0],size[1],3), dtype='uint8')

    vetor_mediana=np.zeros(w_size*w_size)
    

    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            #soma = 0
            #k = 0
            for r in range(3):
                k = 0
                for u in range(w_size):
                    for v in range(w_size):
                        vetor_mediana[k] = f[i-(w_size//2)+u][j-(w_size//2)+v][r]
                        k = k+1
                            
                vetor_mediana = sorted(vetor_mediana)
                g[i][j][r] = vetor_mediana[int((w_size*w_size)/2+1)]     
    return g       

#####################################################################################
#           mediana com imagem CMY...
def mediana_CMY(f,w_size):

    size = f.shape

    g = np.zeros((size[0],size[1],3), dtype='uint8')

    vetor_mediana=np.zeros(w_size*w_size)
    

    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            #soma = 0
            #k = 0
            for r in range(3):
                k = 0
                for u in range(w_size):
                    for v in range(w_size):
                        vetor_mediana[k] = f[i-(w_size//2)+u][j-(w_size//2)+v][r]
                        k = k+1
                            
                vetor_mediana = sorted(vetor_mediana)
                g[i][j][r] = vetor_mediana[int((w_size*w_size)/2+1)]     
    return g       
#####################################################################################
#           mediana com imagem HSI...
def mediana_HSI(f,w_size):

    size = f.shape

    g = np.zeros((size[0],size[1],3), dtype='uint8')

    vetor_mediana=np.zeros(w_size*w_size)
    

    for i in range(size[0]-w_size//2):
        for j in range(size[1]-w_size//2):
            #soma = 0
            #k = 0
            for r in range(3):
                k = 0
                for u in range(w_size):
                    for v in range(w_size):
                        vetor_mediana[k] = f[i-(w_size//2)+u][j-(w_size//2)+v][r]
                        k = k+1
                            
                vetor_mediana = sorted(vetor_mediana)
                g[i][j][r] = vetor_mediana[int((w_size*w_size)/2+1)]     
    return g       

#####################################################################################
if __name__ == '__main__':
    main()
