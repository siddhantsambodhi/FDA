from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
import face_recognition
import os

def FindEncodings(images):
    encodelist=[]
    for imgs in images:
        imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
        imgs=face_recognition.face_encodings(imgs)[0]
        encodelist.append(imgs)
    return encodelist


# Flask constructor
app = Flask(__name__)


def faces():
    name = ''
    if request.method == "POST":


            # # getting input with name = fname in HTML form
            # first_name = request.form.get("fname")
            # # getting input with name = lname in HTML form
            # last_name = request.form.get("lname")
        path = 'Faces'
        images = []
        AllFaces = []
        MyList = os.listdir(path)
        for face in MyList:
                currentImage = cv2.imread(f'{path}/{face}')
                images.append(currentImage)
                AllFaces.append(os.path.splitext(face)[0])
        print(AllFaces)

        encodelistKnown = FindEncodings(images)
        print("encoding complete")
        print(len(encodelistKnown))
        flag = 0
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        try:
                while flag == 0:
                    success, img = cap.read()

                    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                    imgs = cv2.cvtColor(imgs, cv2.COLOR_Luv2LRGB)

                    currentFrameFace = face_recognition.face_locations(imgs)
                    currentFaceEncode = face_recognition.face_encodings(imgs, currentFrameFace)

                    for encode, facelocation in zip(currentFaceEncode, currentFrameFace):
                        match = face_recognition.compare_faces(encodelistKnown, encode)
                        FaceDistance = face_recognition.face_distance(encodelistKnown, encode)
                        # print(FaceDistance)
                        matchIndex = np.argmin(FaceDistance)

                        if match[matchIndex]:
                            name = AllFaces[matchIndex].upper()
                            print(name)
                            flag = 1
                            # connect to db and rectrive all the informantion comes with this name
                            # return name

                    #         if this name is in database, give access to his page(login) just print his/her name into it

                    cv2.imshow('webcam', img)
                    cv2.waitKey(1)
                return name
        except:
            pass
        return name
class DataStore():
    name = None

data=DataStore()
# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():

    # return redirect(url_for("profile"))
    # if name!="None":
    #     return render_template("login.html",name="not found")
    # else:
    #     return render_template("profile.html",name=name)
    name=faces()

    return render_template("profile.html",name=name)

@app.route('/profile', methods=["GET", "POST"])
def profile():

    name2=data.name


    return render_template("profile.html",name=name2)

# @app.route('/form.html', methods=["POST"])
# def print():
#
#     name=""
#     # name=gfg()
#     return render_template("index.html",name="hello")



if __name__ == '__main__':
    app.run()





