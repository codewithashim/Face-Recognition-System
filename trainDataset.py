import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np


class TrainDataset:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1950x1030+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = tk.Label(self.root, text="TRAIN DATA SET", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0,  width=1950, height=45)

        # Top Image
        top_img_path1 = (r"Images/facialrecognition.png")
        img1 = Image.open(top_img_path1)
        img1 = img1.resize((1950, 325), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = tk.Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=47, width=1950, height=325)

        # Button Frame
        train_btn = tk.Button(self.root, text="Train Data", cursor="hand2", command=self.train_classifier, font=(
            "times new roman", 40, "bold"), bg="blue", fg="white", width=1950)
        train_btn.place(x=0, y=380, width=1950, height=80)

        # Bottom Image
        bottom_img_path1 = (r"Images/facial_recognition_action.jpg")
        img2 = Image.open(bottom_img_path1)
        img2 = img2.resize((1950, 550), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = tk.Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=0, y=460, width=1950, height=550)

    # def train_classifier(self):
    #     dataset_path = "dataset"

    #     # Create a list to store the faces and labels
    #     faces = []
    #     labels = []

    #     # Iterate over the folders in the dataset directory
    #     for folder_name in os.listdir(dataset_path):
    #         folder_path = os.path.join(dataset_path, folder_name)
    #         if not os.path.isdir(folder_path):
    #             continue

    #         label = int(folder_name)  # Convert folder name to integer label

    #         # Iterate over the images in the folder
    #         for image_name in os.listdir(folder_path):
    #             image_path = os.path.join(folder_path, image_name)
    #             if not os.path.isfile(image_path):
    #                 continue

    #             # Read the image and convert it to grayscale
    #             image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    #             # Add the face and label to the lists
    #             faces.append(image)
    #             labels.append(label)

    #     # Create an LBPH Face Recognizer
    #     recognizer = cv2.face.LBPHFaceRecognizer_create()

    #     # Train the recognizer using the faces and labels
    #     recognizer.train(faces, np.array(labels))

    #     # Save the trained recognizer to a file
    #     recognizer.save("trained_model.xml")

    #     messagebox.showinfo(
    #         "Success", "Training completed successfully", parent=self.root)
    
    def train_classifier(self):
            

if __name__ == "__main__":
    root = tk.Tk()
    obj = TrainDataset(root)
    root.mainloop()
