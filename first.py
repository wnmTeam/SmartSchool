from mtcnn import MTCNN
import cv2
import os


def detectFromImage(image):
    img = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)
    detector = MTCNN()
    facesInfo = detector.detect_faces(img)
    faces = []
    for faceInfo in facesInfo:
        x, y, w, h = faceInfo['box']
        face = img[y:y + h, x:x + w]
        faces.append(face)
    return faces

def getFacesFromFolder(path):
    facesList = []
    imgsNames = os.listdir(path)
    for name in imgsNames:
        imgPath = os.path.join(path, name)
        faces = detectFromImage(cv2.imread(imgPath))
        for face in faces:
            facesList.append(face)
    return facesList


detectFromImage('1.jpg')
