import cv2
import numpy as np
import face_recognition
import os

# /////////////////////////////////////to encode images from given path(folder)/////////////////////////
def FindEncodings(images):
    encodelist=[]
    for imgs in images:
        imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
        imgs=face_recognition.face_encodings(imgs)[0]
        encodelist.append(imgs)
    return encodelist
# /////////////////////////////////////////////////////////////////////////////////////////


#         /////////////////just to referance////////////////
# Trainimage=cv2.cvtColor(Trainimage,cv2.COLOR_BGR2RGB)
# Testimage=face_recognition.load_image_file('images/test.jpg')
# TrainFace=face_recognition.face_locations(Trainimage)[0]
# encodeTrainFace= face_recognition.face_encodings(Trainimage)[0]
# //////////////////////////////////////////////////////////////////////////////////

# //////get all the images and save them into list
path = 'Faces'
images=[]
AllFaces=[]
MyList=os.listdir(path)
for face in MyList:
    currentImage=cv2.imread(f'{path}/{face}')
    images.append(currentImage)
    AllFaces.append(os.path.splitext(face)[0])
print(AllFaces)


# ///////////////////////////////////////



encodelistKnown= FindEncodings(images)
print("encoding complete")
print(len(encodelistKnown))

def compair():
    cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)
    flag=0
    name=""
    try:
        while flag==0:
            success, img = cap.read()

            imgs =cv2.resize(img,(0,0),None,0.25,0.25)
            imgs =cv2.cvtColor(imgs,cv2.COLOR_Luv2LRGB)

            currentFrameFace=face_recognition.face_locations(imgs)
            currentFaceEncode=face_recognition.face_encodings(imgs,currentFrameFace)

            for encode,facelocation in zip(currentFaceEncode,currentFrameFace):
                match=face_recognition.compare_faces(encodelistKnown,encode)
                FaceDistance=face_recognition.face_distance(encodelistKnown,encode)
                # print(FaceDistance)
                matchIndex=np.argmin(FaceDistance)

                if match[matchIndex]:
                    name= AllFaces[matchIndex].upper()
                    # print(name)
                    flag=1
            #         if this name is in database, give access to his page(login) just print his/her name into it


            cv2.imshow('webcam',img)
            cv2.waitKey(1)
    except:
        pass
    return name

print(compair())


