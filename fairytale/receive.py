from flask import Flask, Response, request
import cv2
import numpy as np
import jsonpickle
import matplotlib.pyplot as plt

app = Flask(__name__)
app.debug = True

def showImage(img):
    plt.imshow(img)
    plt.show()


@app.route('/img/getImage', methods=['POST'])
def receive():
    nparr = np.fromstring(request.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # print(img)
    showImage(img)
    response = {'message':'image: received. size={}x{}'.format(img.shape[0], img.shape[1])}

    # encode response
    response = jsonpickle.encode(response)
    return Response(response=response, status = 200, mimetype='application/json')

if __name__=='__main__':
    app.run(host='0.0.0.0', port = 5001)