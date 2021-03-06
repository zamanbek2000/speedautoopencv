import cv2
import time

cascade_src = 'cars1.xml'
video_src = 'cars02.MP4'
# line a
ax1 = 140
ay = 135
ax2 = 750
# line b
bx1 = 120
by = 180
bx2 = 750
# car num
i = 1
start_time = time.time()
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)


def Speed_Cal(time):
    try:
        Speed = (3.14 * 3600) / (time * 1000)
        return Speed
    except ZeroDivisionError:
        print(5)


while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    # bluring to have exacter detection
    blurred = cv2.blur(img, ksize=(8, 10))
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.2, 3)

    # line a #i know road has got
    cv2.line(img, (ax1, ay), (ax2, ay), (255, 0, 0), 2)
    # line b
    cv2.line(img, (bx1, by), (bx2, by), (255, 0, 0), 2)

    for (x, y, w, h) in cars:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.circle(img, (int((x + x + w) / 2), int((y + y + h) / 2)), 1, (0, 0, 255), -1)

        while int(ay) == int((y + y + h) / 2):
            start_time = time.time()
            break

        while int(ay) <= int((y + y + h) / 2):
            if int(by) <= int((y + y + h) / 2) & int(by + 10) >= int((y + y + h) / 2):
                cv2.line(img, (bx1, by), (bx2, by), (144, 144, 144), 2)
                Speed = Speed_Cal(time.time() - start_time)
                print("Car Number " + str(i) + " Speed: " + str(Speed))
                i = i + 1
                cv2.putText(img, "Speed: " + str(Speed) + "KM/H", (x, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),
                            2);
                break
            else:
                cv2.putText(img, "Calculating", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                break

    cv2.imshow('video', img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
