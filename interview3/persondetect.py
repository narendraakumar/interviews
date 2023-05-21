import cv2
import numpy as np


class PersonDetection:
    def __init__(self, weight_path="dnn_model/yolov4.weights", config_path="dnn_model/yolov4.cfg",
                 classes_file="dnn_model/classes.txt"):
        print("Loading Object Detection")
        print("Running opencv dnn with YOLOv4")
        self.nmsThreshold = 0.4
        self.confThreshold = 0.5
        self.image_size = 700
        self.weight_path = weight_path
        self.config_path = config_path
        self.classes_file = classes_file
        self.load_model()


    def load_model(self):
        net = cv2.dnn.readNet(self.weight_path, self.config_path)
        # if GPU CUDA is available
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.model = cv2.dnn_DetectionModel(net)
        self.classes = ["person"]
        self.colors = np.random.uniform(0, 255, size=(80, 3))
        self.colors = np.random.uniform(0, 255, size=(80, 3))
        self.model.setInputParams(size=(self.image_size, self.image_size), scale=1/255)

    def detect(self, frame):
        return self.model.detect(frame, nmsThreshold=self.nmsThreshold, confThreshold=self.confThreshold)

