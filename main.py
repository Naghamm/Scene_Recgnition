from flask import Flask,redirect,url_for,request,jsonify,send_file,make_response
from skimage import io
import skimage
from Test import recognize_scene

app = Flask(__name__)

@app.route('/')
def home():
    return "Scene Recognition API"
    
@app.route('/Scene_Recognition/', methods =['POST'])
def scene_recognition():
    image_data = request.files['image']
    image = skimage.io.imread(image_data)
    scene = recognize_scene(image)
    return jsonify(scene)

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , threaded = True , debug=True)
