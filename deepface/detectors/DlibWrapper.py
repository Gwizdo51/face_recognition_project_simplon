from pathlib import Path
import gdown
import bz2
import os

def build_model():

    home = str(Path.home())

    import dlib #this requirement is not a must that's why imported here

    #check required file exists in the home/.deepface/weights folder
    # if os.path.isfile(home+'/.deepface/weights/shape_predictor_5_face_landmarks.dat') != True:

    #     print("shape_predictor_5_face_landmarks.dat.bz2 is going to be downloaded")

    #     url = "http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2"
    #     output = home+'/.deepface/weights/'+url.split("/")[-1]

    #     gdown.download(url, output, quiet=False)

    #     zipfile = bz2.BZ2File(output)
    #     data = zipfile.read()
    #     newfilepath = output[:-4] #discard .bz2 extension
    #     # open(newfilepath, 'wb').write(data)
    #     with open(newfilepath, 'wb') as f:
    #         f.write(data)

    # face_detector = dlib.get_frontal_face_detector()
    # sp = dlib.shape_predictor(home+"/.deepface/weights/shape_predictor_5_face_landmarks.dat")

    model_weights_path = Path(__file__).resolve().parent.parent / "model_weights" / 'shape_predictor_5_face_landmarks.dat'

    if not model_weights_path.is_file():
        print("downloading shape_predictor_5_face_landmarks.dat.bz2...")

        url = "http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2"
        model_weights_bz2_path = model_weights_path.parent / url.split("/")[-1]

        gdown.download(url, str(model_weights_bz2_path), quiet=False)

        bz2_file = bz2.BZ2File(str(model_weights_bz2_path))
        data = bz2_file.read()
        with open(model_weights_path, 'wb') as f:
            f.write(data)

    face_detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(str(model_weights_path))

    detector = {}
    detector["face_detector"] = face_detector
    detector["sp"] = sp
    return detector

def detect_face(detector, img, align = True):

    import dlib #this requirement is not a must that's why imported here

    home = str(Path.home())

    sp = detector["sp"]

    detected_face = None
    img_region = [0, 0, img.shape[0], img.shape[1]]

    face_detector = detector["face_detector"]
    detections = face_detector(img, 1)

    if len(detections) > 0:

        for idx, d in enumerate(detections):
            left = d.left(); right = d.right()
            top = d.top(); bottom = d.bottom()
            detected_face = img[top:bottom, left:right]
            img_region = [left, top, right - left, bottom - top]
            break #get the first one

        if align:
            img_shape = sp(img, detections[0])
            detected_face = dlib.get_face_chip(img, img_shape, size = detected_face.shape[0])

    return detected_face, img_region

def detect_faces(detector, img, align = True):

    import dlib #this requirement is not a must that's why imported here

    home = str(Path.home())

    sp = detector["sp"]

    detected_faces_images = []
    img_regions_list = []

    face_detector = detector["face_detector"]
    detections = face_detector(img, 1)
    # detections is of type _dlib_pybind11.rectangles, and made of _dlib_pybind11.rectangle

    for rectangle in detections:

        left = rectangle.left()
        right = rectangle.right()
        top = rectangle.top()
        bottom = rectangle.bottom()

        detected_face_img = img[top:bottom, left:right]
        box = [left, top, right - left, bottom - top]

        if align:
            img_shape = sp(img, rectangle)
            detected_face_img = dlib.get_face_chip(img, img_shape, size = detected_face_img.shape[0])

        detected_faces_images.append(detected_face_img)
        img_regions_list.append(box)

    return detected_faces_images, img_regions_list