import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from bson import ObjectId
import cv2
import os
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access environment variables
database_url = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")
students_collection = os.getenv("STUDENT_DB_COLLECTION")

try:
    client = MongoClient(database_url)

    print("Connected to MongoDB successfully!")

except ConfigurationError as e:
    print("Error: Failed to connect to MongoDB.")
    print("ConfigurationError:", str(e))

except Exception as e:
    print("Error: An unexpected error occurred.")
    print("Exception:", str(e))

collection = client[db_name][students_collection]

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1950x1030+0+0")
        self.root.title("Face Recognition System")

        # ================ Variables ==================

        self.var_dep = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_semester = tk.StringVar()
        self.var_std_id = tk.StringVar()
        self.var_std_name = tk.StringVar()
        self.var_div = tk.StringVar()
        self.var_roll = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_teacher = tk.StringVar()

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
        title_lbl = tk.Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1950, height=45)

        main_frame = tk.Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1900, height=800)

        # Left Label Frame

        Left_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE,
                                   text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=930, height=760)

        img_left = Image.open(
            "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/facial-recognition.jpg")
        img_left = img_left.resize((920, 160), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = tk.Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=920, height=160)

        # Current Course
        current_course_frame = tk.LabelFrame(Left_frame, bd=2, bg="white", relief=tk.RIDGE,
                                             text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=140, width=920, height=130)

        # Department

        dep_label = tk.Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=tk.W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department",
                               "Computer Science", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=tk.W)

        # Course

        course_label = tk.Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=tk.W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=tk.W)

        # Year

        year_label = tk.Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=tk.W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2019-20", "2020-21",
                                "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=tk.W)

        # Semester

        semester_label = tk.Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=tk.W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        semester_combo["values"] = (
            "Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=tk.W)

        # Class Student Information

        class_student_frame = tk.LabelFrame(Left_frame, bd=2, bg="white", relief=tk.RIDGE,
                                            text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=270, width=920, height=400)

        # Student ID

        studentID_label = tk.Label(class_student_frame, text="Student ID:", font=(
            "times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, sticky=tk.W)

        studentID_entry = tk.Entry(class_student_frame, textvariable=self.var_std_id, font=(
            "times new roman", 12, "bold"), bg="lightyellow", width=20)
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Student Name

        studentName_label = tk.Label(class_student_frame, text="Student Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, sticky=tk.W)

        studentName_entry = tk.Entry(class_student_frame, textvariable=self.var_std_name, font=(
            "times new roman", 12, "bold"), bg="lightyellow")
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

        # Class Division

        classDivision_label = tk.Label(class_student_frame, text="Class Division:", font=(
            "times new roman", 12, "bold"), bg="white")
        classDivision_label.grid(row=1, column=0, padx=10, sticky=tk.W)

        classDivision_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), state="readonly", )
        classDivision_combo["values"] = (
            "Select Class Division", "A", "B", "C")
        classDivision_combo.current(0)
        classDivision_combo.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Roll No
        rollNo_label = tk.Label(class_student_frame, text="Roll No:", font=(
            "times new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, sticky=tk.W)

        rollNo_entry = tk.Entry(class_student_frame, textvariable=self.var_roll, font=(
            "times new roman", 12, "bold"), bg="lightyellow")
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)

        # Email
        email_label = tk.Label(class_student_frame, text="Email:", font=(
            "times new roman", 12, "bold"), bg="white")
        email_label.grid(row=2, column=0, padx=10, sticky=tk.W)

        email_entry = tk.Entry(class_student_frame, textvariable=self.var_email, font=(
            "times new roman", 12, "bold"), bg="lightyellow")
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Phone No
        phoneNo_label = tk.Label(class_student_frame, text="Phone No:", font=(
            "times new roman", 12, "bold"), bg="white")
        phoneNo_label.grid(row=2, column=2, padx=10, sticky=tk.W)

        phoneNo_entry = tk.Entry(class_student_frame, textvariable=self.var_phone, font=(
            "times new roman", 12, "bold"), bg="lightyellow")
        phoneNo_entry.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)

        # Address
        address_label = tk.Label(class_student_frame, text="Address:", font=(
            "times new roman", 12, "bold"), bg="white")
        address_label.grid(row=3, column=0, padx=10, sticky=tk.W)

        address_entry = tk.Entry(class_student_frame, textvariable=self.var_address, font=(
            "times new roman", 12, "bold"), bg="lightyellow")
        address_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Gender

        gender_label = tk.Label(class_student_frame, text="Gender:", font=(
            "times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=3, column=2, padx=10, sticky=tk.W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly", )
        gender_combo["values"] = (
            "Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)

        # DOB
        dob_label = tk.Label(class_student_frame, text="DOB:", font=(
            "times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=4, column=0, padx=10, sticky=tk.W)

        dob_entry = tk.Entry(class_student_frame, textvariable=self.var_dob, font=(
            "times new roman", 12, "bold"), bg="lightyellow")
        dob_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        # Teacher Name
        teacherName_label = tk.Label(class_student_frame, text="Teacher Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        teacherName_label.grid(row=4, column=2, padx=10, sticky=tk.W)

        teacherName_entry = tk.Entry(class_student_frame, textvariable=self.var_teacher, font=(
            "times new roman", 12, "bold"), bg="lightyellow")
        teacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=tk.W)

        # Radio Buttons
        self.var_radio1 = tk.StringVar()
        radiobtn1 = tk.Radiobutton(class_student_frame,  variable=self.var_radio1,  text="Take Photo Sample", value="Yes", font=(
            "times new roman", 12, "bold"), bg="white")
        radiobtn1.grid(row=5, column=0, padx=10, pady=2, sticky=tk.W)

        self.var_radio2 = tk.StringVar()
        radiobtn2 = tk.Radiobutton(class_student_frame, variable=self.var_radio2, text="No Photo Sample", value="No", font=(
            "times new roman", 12, "bold"), bg="white")
        radiobtn2.grid(row=5, column=1, padx=10, pady=2, sticky=tk.W)

        # Button Frame
        btn_frame = tk.Frame(class_student_frame, bd=2,
                             relief=tk.RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=910, height=35)

        save_btn = tk.Button(btn_frame, text="Save",  command=self.addStudent, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=25)
        save_btn.grid(row=0, column=0)

        update_btn = tk.Button(btn_frame, text="Update", command=self.updateStudent, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=25)
        update_btn.grid(row=0, column=1)

        delete_btn = tk.Button(btn_frame, text="Delete", command=self.deleteStudent, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=25)
        delete_btn.grid(row=0, column=2)

        reset_btn = tk.Button(btn_frame, text="Reset", command=self.resetData, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=25)
        reset_btn.grid(row=0, column=3)

        # Button Frame 2

        btn_frame2 = tk.Frame(class_student_frame, bd=2,
                              relief=tk.RIDGE, bg="white")
        btn_frame2.place(x=0, y=260, width=910, height=35)

        take_photo_btn = tk.Button(btn_frame2, command=self.generate_dataset, text="Take Photo Sample", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=55)
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = tk.Button(btn_frame2, text="Update Photo Sample", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=55)
        update_photo_btn.grid(row=0, column=1)

        # Right Label Frame

        Right_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE,
                                    text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=960, y=10, width=930, height=760)

        img_right = Image.open(
            "/home/codewithashim/Web Application Drive/Programmer Lab/Advance Face Recognigection/Images/facial-recognition.jpg")
        img_right = img_right.resize((920, 160), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = tk.Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=5, y=0, width=920, height=160)

        # Search System

        search_frame = tk.LabelFrame(Right_frame, bd=2, bg="white", relief=tk.RIDGE,
                                     text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=140, width=920, height=70)

        search_label = tk.Label(search_frame, text="Search By:", font=(
            "times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=tk.W)

        search_entry = tk.Entry(search_frame, font=(
            "times new roman", 12, "bold"), bg="lightyellow", width=20)
        search_entry.grid(row=0, column=2, padx=20, pady=5, sticky=tk.W)

        search_btn = tk.Button(search_frame, text="Search", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = tk.Button(search_frame, text="Show All", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        showAll_btn.grid(row=0, column=4, padx=4)

        # ========================== Table Frame ==========================

        table_frame = tk.Frame(Right_frame, bd=2, bg="white", relief=tk.RIDGE)
        table_frame.place(x=5, y=210, width=920, height=500)

        # Scroll Bar
        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                          "dob", "phone", "email", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Heading

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.pack(fill=tk.BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        students = collection.find()

        self.student_table.delete(*self.student_table.get_children())

        for student in students:
            self.student_table.insert("", tk.END, values=(
                student["Department"],
                student["Course"],
                student["Year"],
                student["Semester"],
                student["StudentID"],
                student["StudentName"],
                student["Division"],
                student["RollNo"],
                student["Gender"],
                student["DOB"],
                student["Phone"],
                student["Email"],
                student["Address"],
                student["TeacherName"],
                student["TakePhotoSample"],
            ))

    # ================ Get Cursor ==================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        students = content["values"]

        self.var_dep.set(students[0])
        self.var_course.set(students[1])
        self.var_year.set(students[2])
        self.var_semester.set(students[3])
        self.var_std_id.set(students[4])
        self.var_std_name.set(students[5])
        self.var_div.set(students[6])
        self.var_roll.set(students[7])
        self.var_gender.set(students[8])
        self.var_dob.set(students[9])
        self.var_phone.set(students[10])
        self.var_email.set(students[11])
        self.var_address.set(students[12])
        self.var_teacher.set(students[13])
        self.var_radio1.set(students[14])

    def update_table(self):
        self.student_table.delete(*self.student_table.get_children())
        students = collection.find()
        for student in students:
            self.student_table.insert("", tk.END, values=(
                student["Department"],
                student["Course"],
                student["Year"],
                student["Semester"],
                student["StudentID"],
                student["StudentName"],
                student["Division"],
                student["RollNo"],
                student["Gender"],
                student["DOB"],
                student["Phone"],
                student["Email"],
                student["Address"],
                student["TeacherName"],
                student["TakePhotoSample"],
            ))

    def addStudent(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            student_id = self.var_std_id.get()
            roll_no = self.var_roll.get()
            existing_student = collection.find_one(
                {"$or": [{"StudentID": student_id}, {"RollNo": roll_no}]})
            if existing_student:
                messagebox.showerror(
                    "Error", "Student ID or RollNo already exists", parent=self.root)
            else:
                student_data = {
                    "Department": self.var_dep.get(),
                    "Course": self.var_course.get(),
                    "Year": self.var_year.get(),
                    "Semester": self.var_semester.get(),
                    "StudentID": self.var_std_id.get(),
                    "StudentName": self.var_std_name.get(),
                    "Division": self.var_div.get(),
                    "RollNo": self.var_roll.get(),
                    "Gender": self.var_gender.get(),
                    "DOB": self.var_dob.get(),
                    "Email": self.var_email.get(),
                    "Phone": self.var_phone.get(),
                    "Address": self.var_address.get(),
                    "TeacherName": self.var_teacher.get(),
                    "TakePhotoSample": self.var_radio1.get(),
                    "NoPhotoSample": self.var_radio2.get()
                }
                result = collection.insert_one(student_data)
                if result.acknowledged:
                    messagebox.showinfo(
                        "Success", "Student Added Successfully", parent=self.root)
                    self.update_table()  # Call the method to update the table
                else:
                    messagebox.showerror(
                        "Error", "Failed to add student", parent=self.root)
    # +++++++++ function +++++++

    # Update Data

    def updateStudent(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            Update = messagebox.askyesno(
                "Update", "Do you want to update this student details", parent=self.root)
            if Update > 0:
                #  Update data in db
                student_data = {
                    "Department": self.var_dep.get(),
                    "Course": self.var_course.get(),
                    "Year": self.var_year.get(),
                    "Semester": self.var_semester.get(),
                    "StudentID": self.var_std_id.get(),
                    "StudentName": self.var_std_name.get(),
                    "Division": self.var_div.get(),
                    "RollNo": self.var_roll.get(),
                    "Gender": self.var_gender.get(),
                    "DOB": self.var_dob.get(),
                    "Email": self.var_email.get(),
                    "Phone": self.var_phone.get(),
                    "Address": self.var_address.get(),
                    "TeacherName": self.var_teacher.get(),
                    "TakePhotoSample": self.var_radio1.get(),
                    "NoPhotoSample": self.var_radio2.get()
                }
                update = collection.update_one(
                    {"StudentID": self.var_std_id.get()}, {"$set": student_data})
                if update.acknowledged:
                    messagebox.showinfo(
                        "Success", "Student details updated successfully", parent=self.root)
                    self.update_table()
                else:
                    messagebox.showerror(
                        "Error", "Failed to update student details", parent=self.root)
            else:
                return None  # Do nothing

    # Delete Data
    def deleteStudent(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showerror(
                "Error", "No student selected", parent=self.root)
            return

        confirmed = messagebox.askyesno(
            "Confirm Deletion", "Are you sure you want to delete the selected student?", parent=self.root)
        if not confirmed:
            return
        for item in selected_item:
            student_id = self.student_table.item(item, "values")[4]
            result = collection.delete_one({"StudentID": student_id})
            if result.acknowledged:
                self.student_table.delete(item)
                messagebox.showinfo(
                    "Success", "Student deleted successfully", parent=self.root)
            else:
                messagebox.showerror(
                    "Error", "Failed to delete student", parent=self.root)

    # Reset Data

    def resetData(self):
        # Clear input fields
        self.var_dep.set("Select Department")
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set(0)
        self.var_radio2.set(0)

        # Refresh table view
        self.student_table.delete(*self.student_table.get_children())

        students = collection.find()
        for student in students:
            self.student_table.insert("", tk.END, values=(
                student["Department"],
                student["Course"],
                student["Year"],
                student["Semester"],
                student["StudentID"],
                student["StudentName"],
                student["Division"],
                student["RollNo"],
                student["Gender"],
                student["DOB"],
                student["Phone"],
                student["Email"],
                student["Address"],
                student["TeacherName"],
                student["TakePhotoSample"],
            ))

        messagebox.showinfo(
            "Success", "Data reset successful", parent=self.root)

    # ============ Genaret data set or take photo sample ==============

    def generate_dataset(self):
        student_id = self.var_std_id.get()

        # Check if the student ID is provided
        if student_id == "":
            messagebox.showerror(
                "Error", "Please enter a Student ID", parent=self.root)
            return

        # Query the database to find the student with the provided ID
        student = collection.find_one({"StudentID": student_id})

        if student:
            # Update the student data
            updated_data = {
                "TakePhotoSample": True,  # Set the TakePhotoSample field to True
                # Update other fields if needed
            }
            collection.update_one({"_id": student["_id"]}, {
                                  "$set": updated_data})

            # Load the face classifier
            face_classifier = cv2.CascadeClassifier(
                "haarcascade_frontalface_default.xml")

            # Capture video from webcam
            video_capture = cv2.VideoCapture(0)

            # Create a directory to store the dataset if it doesn't exist
            dataset_path = "dataset"
            if not os.path.exists(dataset_path):
                os.makedirs(dataset_path)

            # Initialize variables
            sample_count = 0
            max_samples = 50  # Maximum number of samples to capture

            while True:
                ret, frame = video_capture.read()

                # Convert the frame to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces in the grayscale frame
                faces = face_classifier.detectMultiScale(
                    gray, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in faces:
                    # Save the captured face region as an image in the dataset directory
                    image_path = f"{dataset_path}/{student_id}_{str(sample_count).zfill(3)}.jpg"
                    cv2.imwrite(image_path, frame[y:y+h, x:x+w])

                    sample_count += 1

                    # Check if the maximum number of samples is reached
                    if sample_count >= max_samples:
                        break

                    # Draw a rectangle around the detected face on the frame
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Display the frame
                cv2.imshow("Capture", frame)

                # Check if the 'q' key is pressed to stop capturing
                if cv2.waitKey(1) & 0xFF == ord('q') or sample_count >= max_samples:
                    break

            # Release the video capture object and close the OpenCV windows
            video_capture.release()
            cv2.destroyAllWindows()

            messagebox.showinfo(
                "Success", "Dataset generated successfully", parent=self.root)
        else:
            messagebox.showerror(
                "Error", "Student ID not found in the database", parent=self.root)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()
