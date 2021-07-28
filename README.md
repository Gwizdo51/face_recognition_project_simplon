# face_recognition

## TODO

- add a function `detect_faces` to OpenCvWrapper.py ***DONE***<br>
- test it ***DONE***
- add a function `draw_boxes` to functions.py (test function for now) ***DONE***
    - input: a cv2 image array and the regions on which to draw the boxes
    - output: a cv2 image with the boxes drawn
- test it ***DONE***
- add a function `detect_faces` to FaceDetector.py ***DONE***
- test it on opencv ***DONE***
- add a function `detect_faces` to functions.py ***DONE***
    - input: a cv2 image array and a detector name
    - output: the list of all faces found as numpy arrays, and a list of all boxes (x,y,w,h) around the faces found on the original image
- test it on opencv ***DONE***
- add a function `preprocess_face_no_detection` to function.py
    - input: a cv2 face image and a target size
    - output: the preprocessed array representing the face image
- test it on opencv
- add a function `represent_no_detection` to DeepFace.py
- test it on opencv
- add a function `find_faces` to DeepFace.py
- test it on opencv

modify more model wrappers if i can