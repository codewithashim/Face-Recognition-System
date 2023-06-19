import sys
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
from trainDataset import TrainDataset
from faceRecognition import FaceRecognition
from attendance import Attendance
import subprocess
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1950x1030+0+0")
        self.root.title("Face Recognition System")

        # 1st Image
        img_path1 = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/Stanford.jpg"
        img1 = Image.open(img_path1)
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = tk.Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # 2nd Image
        img_path2 = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/facialrecognition.png"
        img2 = Image.open(img_path2)
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = tk.Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # 3rd Image
        img_path3 = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/u.jpg"
        img3 = Image.open(img_path3)
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = tk.Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=500, height=130)

        # 4th Image
        img_path4 = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/face-recognition.png"
        img4 = Image.open(img_path4)
        img4 = img4.resize((500, 130), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        f_lbl4 = tk.Label(self.root, image=self.photoimg4)
        f_lbl4.place(x=1500, y=0, width=500, height=130)

        # Bg Image
        img_path_bg = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/bg.jpg"
        img_bg = Image.open(img_path_bg)
        img_bg = img_bg.resize((1950, 900), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = tk.Label(self.root, image=self.photoimg_bg)
        bg_lbl.place(x=0, y=130, width=1950, height=900)

        # Title
        title_lbl = tk.Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1950, height=45)

        # Student Button
        img_path_student = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/student.png"
        img_student = Image.open(img_path_student)
        img_student = img_student.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_student = ImageTk.PhotoImage(img_student)
        b1 = tk.Button(bg_lbl, image=self.photoimg_student,
                       command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = tk.Button(bg_lbl, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect Face Button

        img_path_detect_face = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/detact_face.png"
        img_detect_face = Image.open(img_path_detect_face)
        img_detect_face = img_detect_face.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_detect_face = ImageTk.PhotoImage(img_detect_face)
        b2 = tk.Button(bg_lbl, image=self.photoimg_detect_face,
                       command=self.face_recognition, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_2 = tk.Button(bg_lbl, text="Face Detector", command=self.face_recognition, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_2.place(x=500, y=300, width=220, height=40)

        # Attendance Button

        img_path_attendance = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/Face_attendance.png"
        img_attendance = Image.open(img_path_attendance)
        img_attendance = img_attendance.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_attendance = ImageTk.PhotoImage(img_attendance)
        b3 = tk.Button(bg_lbl, image=self.photoimg_attendance, command=self.attendance, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)
        b3_3 = tk.Button(bg_lbl, text="Attendance", command=self.attendance, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_3.place(x=800, y=300, width=220, height=40)

        # Help Desk Button

        img_path_help_desk = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/help_desk.png"
        img_help_desk = Image.open(img_path_help_desk)
        img_help_desk = img_help_desk.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_help_desk = ImageTk.PhotoImage(img_help_desk)
        b4 = tk.Button(bg_lbl, image=self.photoimg_help_desk, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_4 = tk.Button(bg_lbl, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_4.place(x=1100, y=300, width=220, height=40)

        # Train Data Button

        img_path_train_data = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/train_data.jpg"
        img_train_data = Image.open(img_path_train_data)
        img_train_data = img_train_data.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_train_data = ImageTk.PhotoImage(img_train_data)
        b5 = tk.Button(bg_lbl, command=self.train_dataset,
                       image=self.photoimg_train_data, cursor="hand2")
        b5.place(x=1400, y=100, width=220, height=220)

        b5_5 = tk.Button(bg_lbl, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_5.place(x=1400, y=300, width=220, height=40)

        # Photos Button

        img_path_photos = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/photo_icon.jpg"
        img_photos = Image.open(img_path_photos)
        img_photos = img_photos.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_photos = ImageTk.PhotoImage(img_photos)
        b6 = tk.Button(bg_lbl, command=self.openPhoto,
                       image=self.photoimg_photos, cursor="hand2")
        b6.place(x=200, y=380, width=220, height=220)

        b6_6 = tk.Button(bg_lbl, command=self.openPhoto, text="Photos", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_6.place(x=200, y=580, width=220, height=40)

        # Developer Button

        img_path_developer = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/developer.png"
        img_developer = Image.open(img_path_developer)
        img_developer = img_developer.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_developer = ImageTk.PhotoImage(img_developer)
        b7 = tk.Button(bg_lbl, image=self.photoimg_developer, cursor="hand2")
        b7.place(x=500, y=380, width=220, height=220)

        b7_7 = tk.Button(bg_lbl, text="Developer", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_7.place(x=500, y=580, width=220, height=40)

        # Chatbot Button

        img_path_chatbot = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/chat.jpg"
        img_chatbot = Image.open(img_path_chatbot)
        img_chatbot = img_chatbot.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_chatbot = ImageTk.PhotoImage(img_chatbot)
        b8 = tk.Button(bg_lbl, image=self.photoimg_chatbot, cursor="hand2")
        b8.place(x=800, y=380, width=220, height=220)

        b8_8 = tk.Button(bg_lbl, text="Chatbot", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_8.place(x=800, y=580, width=220, height=40)

        # Exit Button

        img_path_exit = "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/exit.jpg"
        img_exit = Image.open(img_path_exit)
        img_exit = img_exit.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_exit = ImageTk.PhotoImage(img_exit)
        b9 = tk.Button(bg_lbl, image=self.photoimg_exit, cursor="hand2")
        b9.place(x=1100, y=380, width=220, height=220)

        b9_9 = tk.Button(bg_lbl, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b9_9.place(x=1100, y=580, width=220, height=40)

        # =================== Function Buttons =====================

    def student_details(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = Student(self.new_window)

    def openPhoto(self):
        folder_path = "dataset/"

        if sys.platform == "win32":
            subprocess.Popen(f'explorer "{folder_path}"')
        elif sys.platform == "darwin":
            subprocess.Popen(["open", folder_path])
        elif sys.platform.startswith("linux"):
            subprocess.Popen(["xdg-open", folder_path])
        else:
            messagebox.showerror("Error", "Unsupported platform")

    def train_dataset(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = TrainDataset(self.new_window)

    def face_recognition(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)
    
    def attendance(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = Attendance(self.new_window)    


if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
