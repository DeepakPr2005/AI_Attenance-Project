from pyzbar.pyzbar import decode
from PIL import Image
import cv2,time 
import csv
import reader


video = cv2.VideoCapture(0)
students = []

with open("ai-attendence.csv","r") as file:
    reader= csv.reader(file)
    for row in reader:
        students.append(row[1])


while True:
    check,frame= video.read()
    d = decode(frame)
    try:
        for obj in d:
            name = d[0].data.decode()
            if name in students:
                students.remove(name)
                print("deleted ...............................")

    except:
        print("error")


    cv2.imshow("attendence",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        print(students)
        break



video.release()
cv2.destroyAllWindows()


# python manage.py loaddata db.json