from PIL import Image
import math

def  rgbtohsi (R, G, B):

    if(0<=R<=255 and 0<=G<=255 and 0<=B<=255):
       d=R+G+B
       r=R/d
       g=G/d
       b=B/d
       num=0.5*((r-g)+(r-b))
       den=((r-g)*(r-g)+(r-b)*(g-b))**(0.5)

    if(b<=g):

       if den != 0:
           h = math.acos(num / (den))
       else:
           h = 0

    elif(b>g):

        if den!=0:
            h=(2*math.pi)-math.acos(num/den)
        else:
            h=0
    s=1-(3*min(r,g,b))
    i=(R+G+B)/(3*255)

    return int(h*180/math.pi), int(s*100), int(i*255)

image=Image.open("HSI.jpg").convert("RGB")

resim_pix = image.load()

w=image.size[0]

hg=image.size[1]

for i in range(w):

    for j in range(hg):
        r, g, b = image.getpixel((i, j))

        h, s, v = rgbtohsi(r, g, b)

        resim_pix[i,j] = (h, s, v)

image.save("hsi_new.jpg")

image.show()
