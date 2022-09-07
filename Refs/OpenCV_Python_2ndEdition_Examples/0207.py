# 0207.py
import cv2

#cap = cv2.VideoCapture(0)  # 0번 카메라
cap = cv2.VideoCapture('./data/vtest.avi')
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

##
imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile)
resize_img = cv2.resize(img,(300,300))
#cv2.imshow('Lena color',img)
##

while True:   
    retval, frame = cap.read()
    if not retval:
        break
    
    #img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
    text = 'OpenCV Programming'
    org = (50,100)
    org2=(100,200)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text, org, font, 1, (255,0,0), 2)
    
    ##img1 = cv2.imread('frame',frame)
    img1 = cv2.resize(frame,(300,300))
    dst1= cv2.add(img1,resize_img)
    
    cv2.imshow('frame',dst1)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
