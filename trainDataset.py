import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
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
        train_btn = tk.Button(self.root, text="Train Data", cursor="hand2", command=self.train_dataset, font=(
            "times new roman", 40, "bold"), bg="blue", fg="white", width=1950)
        train_btn.place(x=0, y=380, width=1950, height=80)

        # Bottom Image
        bottom_img_path1 = (r"Images/facial_recognition_action.jpg")
        img2 = Image.open(bottom_img_path1)
        img2 = img2.resize((1950, 550), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = tk.Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=0, y=460, width=1950, height=550)

    def train_dataset(self):
        # Load images and labels from the dataset folder
        dataset_path = ("dataset")
        images = []
        labels = []

        for root, dirs, files in os.walk(dataset_path):
            for file in files:
                if file.endswith(".jpg"):
                    image_path = os.path.join(root, file)
                    # Extract the label from the filename
                    label = int(file.split("_")[0])
                    # Read image in grayscale
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    # Resize the image to a consistent shape
                    resized_image = cv2.resize(image, (100, 100))
                    # Flatten image to 1D array
                    images.append(resized_image.flatten())
                    labels.append(label)

                    # Show the image in a window
                    cv2.imshow("Dataset", resized_image)
                    cv2.waitKey(50)  # Display each image for 100 milliseconds

        # Convert images and labels to numpy arrays
        images = np.array(images, dtype=np.float32)
        labels = np.array(labels)

        # Create a KNN classifier and train it
        knn = cv2.ml.KNearest_create()
        knn.train(images, cv2.ml.ROW_SAMPLE, labels)
        
            # Create a "traindata" folder if it doesn't exist
        traindata_path = "traindata"
        if not os.path.exists(traindata_path):
            os.makedirs(traindata_path)

        # Save the trained model inside the "traindata" folder
        model_path = os.path.join(traindata_path, "trained_model.xml")
        knn.save(model_path)

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed")


if __name__ == "__main__":
    root = tk.Tk()
    obj = TrainDataset(root)
    root.mainloop()
