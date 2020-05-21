# Introduction
### Scene_Recognition_API
  - classify scene image to one of ten scene classes.
### API Input
  - Post request with scene image of any type jpg, png ,..etc
### API output
  - string with the scene name
 
# Getting started
1) Build docker image
    $ docker build -t scene_recognition_image .
2) Run docker container
    $ docker run -p 10000 -p 5000:5000 --name scene_recognition_container scene_recognition_image

# Test Scene_Recognition API
1) Using Python script
    import requests
    files = {'image': open("test_image_path" ,'rb')}
    scene = requests.post("http://0.0.0.0:5000/Scene_Recognition/" , files=files)
    print ('Scene: ' , scene.text)
2) Using postman
    -  Make post request on port 5000 with endpoint Scene_Recognition
        http://0.0.0.0:5000/Scene_Recognition/
    -  Add test_image to body with key 'image'

## Note:
# Before running any notebook:
  Run "Data_Preparation.ipynb" notebook first
# Find Approaches Accuacies in:
  https://github.com/Naghamm/Scene_Recognition/Approaches.md
 