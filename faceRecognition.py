import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import face_recognition
import os
import numpy as np
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from bson import ObjectId
import cv2
import bson


uri = "mongodb+srv://codewithashim:ApiBqTIIZ4BYi93h@facerecognition.hjt9mmz.mongodb.net/FaceRecognition?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)

    print("Connected to MongoDB successfully form recog!")

except ConfigurationError as e:
    print("Error: Failed to connect to MongoDB.")
    print("ConfigurationError:", str(e))

except Exception as e:
    print("Error: An unexpected error occurred.")
    print("Exception:", str(e))

collection = client["FaceRecognition"]["Student"]


class FaceRecognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1950x1030+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = tk.Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1950, height=45)

        # Left Image

        img_left = Image.open(r"Images/face_detector1.jpg")
        img_left = img_left.resize((775, 965), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = tk.Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=50, width=775, height=965)

        # Right Image

        img_right = Image.open(r"Images/facedetact2.jpg")
        img_right = img_right.resize((1175, 965), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_rbl = tk.Label(self.root, image=self.photoimg_right)
        f_rbl.place(x=775, y=50, width=1175, height=965)

        # Button Right Image

        b1_1 = tk.Button(f_rbl, text="Face Recognition", command=self.recognize_faces, cursor="hand2",  font=(
            "times new roman", 20, "bold"), bg="green", fg="white")
        b1_1.place(x=470, y=850, width=220, height=50)

    # ================== Face Recognition =====================

    def recognize_faces(self):
        # Load the trained model
        model_path = "traindata/trained_model.xml"
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(model_path)

        # Load the face cascade classifier
        face_cascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")

        # Start video capture from webcam
        video_capture = cv2.VideoCapture(0)

        try:
            while True:
                ret, frame = video_capture.read()

                # Convert the captured frame to grayscale for face detection
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces in the frame
                faces = face_cascade.detectMultiScale(
                    gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                for (x, y, w, h) in faces:
                    # Crop the face region from the frame
                    face_roi = gray_frame[y:y + h, x:x + w]

                    # Recognize the face
                    label, confidence = recognizer.predict(face_roi)

                    if confidence < 100:
                        # Retrieve student data based on StudentID
                        student_data = collection.find_one(
                            {"StudentID": str(label)})

                        if student_data:
                            # Extract student details from the database
                            student_name = student_data["StudentName"]
                            roll_no = student_data["RollNo"]
                            student_id = student_data["StudentID"]

                            # Display student details on the frame
                            cv2.putText(frame, f"Name: {student_name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                        (0, 255, 0), 2)
                            cv2.putText(frame, f"Roll: {roll_no}", (x, y + h + 30),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                            cv2.putText(frame, f"Student ID: {student_id}", (x, y + h + 60),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                        else:
                            cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                        (0, 0, 255), 2)
                            cv2.putText(frame, f"Confidence: {round(confidence, 2)}%", (x, y + h + 30),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    else:
                        cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                    (0, 0, 255), 2)
                        cv2.putText(frame, f"Confidence: {round(confidence, 2)}%", (x, y + h + 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                    # Draw a rectangle around the face
                    cv2.rectangle(frame, (x, y), (x + w, y + h),
                                  (255, 0, 0), 2)

                # Display the frame with recognized faces
                cv2.imshow("Face Recognition", frame)

                # Exit if the 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            # Release the video capture and destroy all windows
            video_capture.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = tk.Tk()
    obj = FaceRecognition(root)
    root.mainloop()
