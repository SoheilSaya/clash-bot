import cv2
from PIL import Image
from pytesseract import pytesseract
import time
import winsound
from pywinauto.application import Application
import keyboard


# Define the path to the Tesseract executable
path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Define the path to the image
image_path = r"image.png"

# Point pytesseract to the Tesseract executable
pytesseract.tesseract_cmd = path_to_tesseract
# Set up the capture object
cap = cv2.VideoCapture(0)

# Set up the video codec and output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
def correctnumber(number):
    number=number.replace("s", "5")
    number=number.replace("S", "5")
    number=number.replace("g", "6")
    number=number.replace("G", "6")
    number=number.replace("I", "1")
    number=number.replace("i", "1")
    number=number.replace("l", "1")
    number=number.replace("L", "1")
    number=number.replace("!", "1")
    number=number.replace(".", "")
    number=number.replace(" ", "")
    number=number.replace(",", "")
    return(number)
        
npressed=False 
lastn=time.time()
# Capture frames from the webcam



def gofind(substance,foundQuantity,wantedQuantity,lastn):
    flag=False
    if substance=='gold' or substance=='elixir':
        if int(foundQuantity)>=wantedQuantity and int(foundQuantity)<2000000:
            lastn=time.time()
            print(f'HIGH {substance}!! >>> {foundQuantity}>{wantedQuantity}')
            winsound.Beep(3000, 200)
            flag=True
        else:
            winsound.Beep(300, 300)
            keyboard.press('N')
            keyboard.release('N')
            lastn=time.time()
            print('nextttt')
    if substance=='dark':
        if int(foundQuantity)>=wantedQuantity and int(foundQuantity)<20000:
            lastn=time.time()
            print(f'HIGH {substance}!! >>> {foundQuantity}>{wantedQuantity}')
            winsound.Beep(3000, 200)
                
        else:
            winsound.Beep(300, 300)
            keyboard.press('N')
            keyboard.release('N')
            lastn=time.time()
            print('nextttt')
    return lastn,flag



while cap.isOpened():
    counter=0
    if counter>10000:
        counter=0
    if counter%5==True:
        keyboard.release('U')
        keyboard.release('Y')
    keyboard.press('Y')
    keyboard.press('U')
    
    print(time.time()-lastn)
    if time.time()-lastn>7:
        winsound.Beep(1000, 100)
        keyboard.press('N')
        keyboard.release('N')
        lastn=time.time()
        print('no input')
    time.sleep(0.5)
    ret, frame = cap.read()
    if ret:
        # Write the frame to the output file
        out.write(frame)

        # Display the frame
        cv2.imshow('frame', frame)
        text = pytesseract.image_to_string(frame)
        lines = text.splitlines()
        #print(text,'text')
 

        try:
            if len(lines)==3 :
                gold=((correctnumber(lines[0])))
                elixir=((correctnumber(lines[1])))
                dark=((correctnumber(lines[2])))
                #print(lines[0],'raw')
                print(gold,'gold')
                print(elixir,'elixir')
                print(dark,'dark')
                substance,foundQuantityy,wantedQuantity='gold',gold,800000
                lastn,flag=gofind(substance,foundQuantityy,wantedQuantity,lastn)
                if flag==True:
                    while True:
                        time.sleep(0.5)
                        #lastn=time.time()
                        print(f'HIGH {substance}!! >>> {foundQuantityy}>{wantedQuantity}')
                        winsound.Beep(3000, 200)
            
        except:
            print(Exception)
            winsound.Beep(300, 300)
            keyboard.press('N')
            keyboard.release('N')
            lastn=time.time()
            print('error')
            pass
  






        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
