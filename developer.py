import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1950x1030+0+0")
        self.root.title("Face Recognition System")

        # Background Image
        img_bg = Image.open(r"Images/dev.jpg")
        img_bg = img_bg.resize((1950, 1030), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_img = tk.Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=0, width=1950, height=1050)

        # Developer Frame
        self.frame1 = tk.Frame(self.root, bg="white")
        self.frame1.place(x=480, y=100, width=1000, height=800)

        # Developer Profile Picture
        img1 = Image.open(r"Images/profile.jpeg")
        img1 = img1.resize((200, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = tk.Label(self.frame1, image=self.photoimg1)
        f_lbl.place(x=350, y=50, width=200, height=200)

        # Developer Label Name

        dev_lbl = tk.Label(self.frame1, text="Developer : Ashim Rudra Paul", font=(
            "times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=50, y=300, width=1000, height=40)

        # Developer Label Email
        dev_lbl = tk.Label(self.frame1, text="Email : codewithashim@gmail.com",
                           font=(
                               "times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=50, y=350, width=1000, height=40)

        # Developer Label Github
        dev_lbl = tk.Label(self.frame1, text="Github : https://github.com/codewithashim", font=(
            "times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=50, y=400, width=1000, height=40)

        # Developer Label Linkedin
        dev_lbl = tk.Label(self.frame1, text="Linkedin : https://www.linkedin.com/in/codewithashim", font=(
            "times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=50, y=450, width=1000, height=40)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Developer(root)
    root.mainloop()
