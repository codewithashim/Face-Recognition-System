import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from bson import ObjectId
import os
import csv
from tkinter import filedialog
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access environment variables
database_url = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")
attendance_collection = os.getenv("ATTENDANCE_DB_COLLECTION")

try:
    client = MongoClient(database_url)
    print("Connected to MongoDB successfully!")

except ConfigurationError as e:
    print("Error: Failed to connect to MongoDB.")
    print("ConfigurationError:", str(e))

except Exception as e:
    print("Error: An unexpected error occurred.")
    print("Exception:", str(e))

collection = client[db_name][attendance_collection]

myData = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1950x1030+0+0")
        self.root.title("Face Recognition System")

        # ============= Variables =================

        self.var_attendanceId = tk.StringVar()
        self.var_rollNumber = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_department = tk.StringVar()
        self.var_time = tk.StringVar()
        self.var_date = tk.StringVar()
        self.var_attendanceStatus = tk.StringVar()

        # Title Label
        title_lbl = tk.Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1950, height=45)

        # Top Image
        img_top = Image.open(r"Images/attendance_image_1.png")
        img_top = img_top.resize((920, 250), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=920, height=250)

        img_top_2 = Image.open(r"Images/attendance_image_2.png")
        img_top_2 = img_top_2.resize((900, 250), Image.ANTIALIAS)
        self.photoimg_top_2 = ImageTk.PhotoImage(img_top_2)

        f_lbl = tk.Label(self.root, image=self.photoimg_top_2)
        f_lbl.place(x=940, y=45, width=900, height=250)

        # Bg Image
        img_bg = Image.open(r"Images/bg.jpg")
        img_bg = img_bg.resize((1950, 1030), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_img = tk.Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=300, width=1950, height=850)

        #  Main Frame
        main_frame = tk.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=10, width=1900, height=700)

        # Left Frame

        left_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE,
                                   text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=850, height=680)

        # Left inside frame
        left_inside_frame = tk.Frame(
            left_frame, bd=2, bg="white", relief=tk.RIDGE)
        left_inside_frame.place(x=5, y=5, width=830, height=620)

        # attendance Id
        attendanceId_label = tk.Label(left_inside_frame, text="Attendance ID:", font=(
            "times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame,textvariable=self.var_attendanceId ,width=20, font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # roll number

        roll_number_label = tk.Label(left_inside_frame, text="Roll Number:", font=(
            "times new roman", 12, "bold"), bg="white")
        roll_number_label.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        roll_number_entry = ttk.Entry(
            left_inside_frame,textvariable=self.var_rollNumber ,width=20, font=("times new roman", 12, "bold"))
        roll_number_entry.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

        # name

        name_label = tk.Label(left_inside_frame, text="Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        name_entry = ttk.Entry(left_inside_frame,textvariable=self.var_name ,width=20,
                               font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # department

        department_label = tk.Label(left_inside_frame, text="Department:", font=(
            "times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)

        department_entry = ttk.Entry(
            left_inside_frame, textvariable=self.var_department,width=20, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)

        # time

        time_label = tk.Label(left_inside_frame, text="Time:", font=(
            "times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_time,width=20,
                               font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # date

        date_label = tk.Label(left_inside_frame, text="Date:", font=(
            "times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)

        date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_date ,width=20,
                               font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)

        # attendance status

        attendance_status_label = tk.Label(left_inside_frame, text="Attendance Status:", font=(
            "times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(
            row=3, column=0, padx=10, pady=5, sticky=tk.W)

        attendance_status = ttk.Combobox(left_inside_frame, textvariable=self.var_attendanceStatus,width=20, font=(
            "times new roman", 12, "bold"), state="readonly")
        attendance_status["values"] = ("Status", "Present", "Absent")
        attendance_status.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        attendance_status.current(0)

        # button frame

        btn_frame = tk.Frame(left_inside_frame, bd=2,
                             relief=tk.RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=820, height=40)

        # Import button

        import_csv_btn = tk.Button(btn_frame, text="Import CSV", command=self.importCsv, width=24, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        import_csv_btn.grid(row=0, column=0)

        # Export button

        export_csv_btn = tk.Button(btn_frame, text="Export", width=24, command=self.exportCsv,font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        export_csv_btn.grid(row=0, column=1)

        # Update button

        updpate_btn = tk.Button(btn_frame, text="Update", command=self.update_data,width=22, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        updpate_btn.grid(row=0, column=2)

        # reset button

        reset_btn = tk.Button(btn_frame,command=self.reset_data ,text="Reset", width=22, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right Label Frame

        Right_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE,
                                    text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=860, y=10, width=990, height=680)

        img_right = Image.open(
            "Images/facial-recognition.jpg")
        img_right = img_right.resize((920, 180), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = tk.Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=5, y=0, width=990, height=180)

        # Table Frame

        table_frame = tk.Frame(Right_frame, bd=2, bg="white", relief=tk.RIDGE)
        table_frame.place(x=5, y=190, width=970, height=450)

        # Scroll Bar Table

        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "attendanceId", "rollNumber", "name", "department", "time", "date", "attendanceStatus"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading(
            "attendanceId", text="Attendance ID")
        self.AttendanceReportTable.heading("rollNumber", text="Roll Number")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading(
            "attendanceStatus", text="Attendance Status")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("attendanceId", width=100)
        self.AttendanceReportTable.column("rollNumber", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendanceStatus", width=100)

        self.AttendanceReportTable.pack(fill=tk.BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content["values"]
        self.var_attendanceId.set(row[0])
        self.var_rollNumber.set(row[1])
        self.var_name.set(row[2])
        self.var_department.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attendanceStatus.set(row[6])

# Fetch Data

    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", "end", values=i)

    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetch_data(myData)

    def exportCsv(self):
        try:
            if len(myData) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Exported", "Your Data Exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content["values"]
        self.var_attendanceId.set(row[0])
        self.var_rollNumber.set(row[1])
        self.var_name.set(row[2])
        self.var_department.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attendanceStatus.set(row[6])

    def reset_data(self):
        self.var_attendanceId.set("")
        self.var_rollNumber.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendanceStatus.set("")

    def update_data(self):
        if self.var_attendanceId.get() == "":
            messagebox.showerror(
                "Error", "Attendance ID must be required", parent=self.root)
        else:
            try:
                update = collection.update_one({"_id": ObjectId(self.var_attendanceId.get())}, {"$set": {
                    "rollNumber": self.var_rollNumber.get(),
                    "name": self.var_name.get(),
                    "department": self.var_department.get(),
                    "time": self.var_time.get(),
                    "date": self.var_date.get(),
                    "attendanceStatus": self.var_attendanceStatus.get()
                }})
                if update.modified_count > 0:
                    messagebox.showinfo(
                        "Success", "Student details updated successfully", parent=self.root)
                    self.show_data()
                else:
                    messagebox.showerror(
                        "Failed", "Failed to update student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Attendance(root)
    root.mainloop()
