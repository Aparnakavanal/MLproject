from flask import Flask, request, jsonify
import face_recognition
import os
import shutil
import urllib.parse

app = Flask(__name__)


@app.route('/pictureFinder', methods=['POST'])
def pictureFinder():
    #os.makedirs('')
    URLpath = request.args.get('path')
    NewURLpath = request.args.get('cretepath')
    print("path",URLpath)
    for file_name in os.listdir(URLpath):
        face_image = face_recognition.load_image_file(os.path.join(URLpath, file_name))
        face_encoding = face_recognition.face_encodings(face_image)[0]
        for picture in os.listdir(NewURLpath):
            pic_image = face_recognition.load_image_file(os.path.join(URLpath, file_name))
            pic_encoding = face_recognition.face_encodings(pic_image)[0]
            match = face_recognition.compare_faces([pic_encoding], face_encoding[0])
            if match[0]:
                print("File Already Exists")
            else:
                shutil.copy(os.path.join(URLpath, file_name), os.path.join(NewURLpath, file_name))
                folder_name = file_name.split('.')[0]
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                for file_name in os.listdir(URLpath):
                    face_image = face_recognition.load_image_file(os.path.join(URLpath, file_name))
                    face_encodings = face_recognition.face_encodings(face_image)
                    if len(face_encodings) > 0:
                        match = face_recognition.compare_faces([face_encoding], face_encodings[0])
                        if match[0]:
                            shutil.copy(os.path.join(URLpath, file_name), os.path.join(folder_name, file_name))
    return jsonify({'message': 'Folder created successfully'})
                


if __name__ == '__main__':
    app.run()
