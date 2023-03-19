from flask import Flask, request, jsonify
import face_recognition
import os
import shutil

app = Flask(__name__)


@app.route('/pictureFinder', methods=['POST'])
def pictureFinder():
    #os.makedirs('')
    for file_name in os.listdir('C:\Arun SK\ML Project\Sample_For_Python_Scripting-20230318T083301Z-001\sample_pic'):
        face_image = face_recognition.load_image_file(os.path.join('C:\Arun SK\ML Project\Sample_For_Python_Scripting-20230318T083301Z-001\sample_pic', file_name))
        face_encoding = face_recognition.face_encodings(face_image)[0]
        for picture in os.listdir('C:\\Arun SK\\ML Project\\Sample_For_Python_Scripting-20230318T083301Z-001\\new_pic'):
            pic_image = face_recognition.load_image_file(os.path.join('C:\Arun SK\ML Project\Sample_For_Python_Scripting-20230318T083301Z-001\sample_pic', file_name))
            pic_encoding = face_recognition.face_encodings(pic_image)[0]
            match = face_recognition.compare_faces([pic_encoding], face_encoding[0])
            if match[0]:
                print("Pass")
            else:
                shutil.copy(os.path.join('C:\Arun SK\ML Project\Sample_For_Python_Scripting-20230318T083301Z-001\sample_pic', file_name), os.path.join('C:\\Arun SK\\ML Project\\Sample_For_Python_Scripting-20230318T083301Z-001\\new_pic', file_name))
                folder_name = file_name.split('.')[0]
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                for file_name in os.listdir('C:\Arun SK\ML Project\Sample_For_Python_Scripting-20230318T083301Z-001\sample_pic'):
                    face_image = face_recognition.load_image_file(os.path.join('C:\Arun SK\ML Project\Sample_For_Python_Scripting-20230318T083301Z-001\sample_pic', file_name))
                    face_encodings = face_recognition.face_encodings(face_image)
                    if len(face_encodings) > 0:
                        match = face_recognition.compare_faces([face_encoding], face_encodings[0])
                        if match[0]:
                            shutil.copy(os.path.join('C:\Arun SK\ML Project\Sample_For_Python_Scripting-20230318T083301Z-001\sample_pic', file_name), os.path.join(folder_name, file_name))
    return jsonify({'message': 'Folder created successfully'})
                


if __name__ == '__main__':
    app.run()
