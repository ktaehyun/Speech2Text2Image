'''
file: appㅍ2.py
author: Guyoung Kwon
date: 2022.09.19
memo:
    이미지 데이터를 base64로 인코딩하고 json에 저장하여 전송하는 모듈
'''
from flask import Flask, render_template, request, url_for, redirect, send_file
import cv2
import requests
import json
import base64

app = Flask(__name__)
app.debug=True

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/getMessage', methods=['POST'])
def getMessage():
    if request.method == 'POST':
        # json 통신을 위한 방법
        if request.is_json:
            txt = request.json['txt']
        else:
            txt = request.form['txt']
        img = 'images/' + txt + '.jpg'
    print(txt)
    # send the image data to other server after processing
    sendMessage(imageProcessing(img), txt)
    
    # return send_file('./아이유.jpg', as_attachment=True) # 파일이 저장됨
    return render_template('index.html', txt=txt, img=img) # 파일을 html화면에서 출력

def imageProcessing(img):
    # get image data
    image = cv2.imread('static/' + img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (720, 480))
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', image)

    return img_encoded

def sendMessage(img, txt):
    # prepare headers for http request
    content_type = 'application/json'
    headers = {'content-type': content_type, 'charset':'utf-8'}
    
    # encoding with base64
    img = base64.b64encode(img).decode('utf-8')
    data = {"title": txt, "img":img}
    data = json.dumps(data)
    # send http request with image and receive response
    response = requests.post('http://192.168.0.23:5001/img/getImage', data=data, headers=headers)
    print(response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)