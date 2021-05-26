import cv2 
import os 
import time
import random
from twython import Twython
path = r'C:\temp'
nameList = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg","11.jpg","12.jpg","13.jpg","14.jpg","15.jpg"]

textList = ["Personally I prefer C# over Python.",
            "You can check out some more of my work over at ignurof.xyz",
            "This is a randomized message pulled from a list of strings.",
            "School assignment in Computer Science, remote school.",
            "My profile picture & cover picture come from the game Haven & Hearth, check it out today!",
            "Add me on Discord if you want to get in contact! Ignurof#5735",
            "Potential uses of the software: overwatch camera security, plant watcher",
            "Another line, another randomized string of bullcrap."]

APP_KEY = 'keyhere'
APP_SECRET = 'wkeyhere'
OAUTH_TOKEN = 'keyhere'
OAUTH_TOKEN_SECRET = 'keyhere'

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

x = 0
y = 15

def randomize():
    rng = random.randint(1,9)
    if rng == 1:
        return textList[0]
    if rng == 2:
        return textList[1]
    if rng == 3:
        return textList[2]
    if rng == 4:
        return textList[3]
    if rng == 5:
        return textList[4]
    if rng == 6:
        return textList[5]
    if rng == 7:
        return textList[6]
    if rng == 8:
        return textList[7]

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

def tweeterup(filename):
    # Öppna bilden i filströmmen
    photo = open('C:/temp/'+filename, 'rb')
    # Spara svaret från twitter
    response = twitter.upload_media(media=photo)
    myText = randomize()
    # Uppdatera status med bild media
    twitter.update_status(status=myText, media_ids=[response['media_id']])

def debugtweet():
    # Kolla om allting fungerar
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    # Läs in bilden, ret === true på lyckad bild
    ret, frame = video_capture.read()
    print("Saving..")
    cv2.imwrite("name.jpg", frame)
    tweeterup("name.jpg")

# Välj sökväg
os.chdir(path)

# Öppna kamera strömmen
video_capture = cv2.VideoCapture(0)

#debugtweet() # - användes för att kolla så appen fungerade korrekt

while x < y:
    countdown(60)   # Vänta 1min
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    ret, frame = video_capture.read()
    print("Saving..")
    # Spara bilden
    cv2.imwrite(nameList[x], frame)
    tweeterup(nameList[x])
    x += 1   

# Stäng kamera strömmen
video_capture.release()


