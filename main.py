import cv2
import numpy as np
import face_recognition





# to train image
Trainimage=face_recognition.load_image_file('images/train.jpg')
Trainimage=cv2.cvtColor(Trainimage,cv2.COLOR_BGR2RGB)



#to test images
Testimage=face_recognition.load_image_file('images/test.jpg')
Testimage=cv2.cvtColor(Testimage,cv2.COLOR_BGR2RGB)




# to find face and generate code
TrainFace=face_recognition.face_locations(Trainimage)[0]
encodeTrainFace= face_recognition.face_encodings(Trainimage)[0]
# cv2.rectangle(Trainimage,(TrainFace[3],TrainFace[0]),(TrainFace[1],TrainFace[2]),(255,0,255),2)
# print(TrainFace,encodeFace)

TestFace=face_recognition.face_locations(Testimage)[0]
encodeTestFace= face_recognition.face_encodings(Testimage)[0]
# cv2.rectangle(Testimage,(TestFace[3],TestFace[0]),(TestFace[1],TestFace[2]),(255,0,255),2)



Result=face_recognition.compare_faces([encodeTrainFace],encodeTestFace)
print(Result)

if Result==[True]:
    print("Match")
else:
    print("Who the hell r u??????????????")

# cv2.imshow('mark',Trainimage)
# cv2.imshow('mark test',Testimage)
cv2.waitKey(0)







#
# from flask import Blueprint, render_template
# from flask_login import login_required, current_user
#
# main = Blueprint('main', __name__)
#
# @main.route('/')
# def index():
#     return render_template('index.html')
#
# @main.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.name)

