import tkinter as tk
from tkinter import *
import tkinter
from tkinter import filedialog
from tkinter import ttk, StringVar, IntVar
from PIL import ImageTk, Image
from tkinter import messagebox
from PIL import Image
import final_sotware
import xlwt
from xlwt import Workbook


def s_exit():
    exit(0)


def putwindow():

    window = Tk()
    window.geometry("800x500")
    #window.configure(background='')
    window.title("Smart Attendance System")
    #window.geometry("800x500")
    tkinter.Label(window, text = "SMART ATTENDANCE SYSTEM", font = 12, fg = "black", bg = "#FBC396").pack(fill = "x")
    tkinter.Label(window, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg = '#FBC396').pack(fill = 'x')
    tkinter.Label(window, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg = '#FBC396').pack(fill = 'x')

    tkinter.Label(window, text = "Created by Dang-Linh Trinh", fg = "black", bg = "salmon1").pack(fill = "x")

    tkinter.Label(window, text = " ").pack(fill = 'y')

    tkinter.Label(window, text = ": \n\n"
                                 "Project: Combining Video Class Solution with Face Recognition Solution\n\n"
                                 "Student Name: Trinh Dang Linh\n\n"
                                 "Class: Advanced Project for AI\n\n"
                                                   , fg = "black", bg = "#98B08B").pack(fill = "y")   #aquamarine
    
    tkinter.Label(window, text = "\n\n").pack(fill = 'y')


    tkinter.Label(window, text = ": \n\n"
                                 "This software includes:\n\n"
                                 "1. Face Detection and Alignment by using MTCNN model \n\n"
                                 "2. Facenet for embedding feature extraction and SVM for Classification (Recognition Task)\n\n\n "

                                 "**************   How to use this application   *************\n\n"

                                 "1) Press 's' keyword to start face detection in video or webcam frames and save the faces for each person.\n"
                                 "   This dataset creation will stop the moment you release the 's' key. This can be done multiple times.\n\n"
                                 "2) Press 'q' to close it when you are done with one person, and want to detect face for another person.\n\n"
                                 "3) Make sure you press the keywords on the image window and not the terminal window.                   \n"
                  , fg = "black", bg = "#C2C2B4").pack(fill = "y")

    def cont_inue():
        window.destroy()
        show()

    btn1 = tkinter.Button(window, text = "CONTINUE", fg = "black", bg = '#F2D388', command = cont_inue)
    btn1.place(x=360, y=450, width=80)




    window.mainloop()


def show():
    #putwindow.window.destroy()
    window2 = Tk()
    window2.title("Smart Attendance System")
    window2.geometry("800x500")
    tkinter.Label(window2, text = "SMART ATTENDANCE SYSTEM", font= 12, fg="black", bg="#FBC396").pack(fill="x")
    tkinter.Label(window2, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg='#FBC396').pack(fill='x')
    tkinter.Label(window2, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg='#FBC396').pack(fill='x')

    #tkinter.Label(window2, text="TEST", fg="lightblue", bg="gray").pack(fill="x")
    tkinter.Label(window2, text = "\n\n ").pack(fill = 'y')


    tkinter.Label(window2, text = "Tutorial for this application:\n\n"
                                  "1. Click 'Train' for making a new classifier when adding new persons.\n\n"
                                  "2. Click 'TEST' to test on previously MTCNN created dataset by loading\n" 
                                  "   new created classifier.\n\n"
                                  "3. Click 'CREATE' to add new person into the existing dataset.\n\n"
                                  "4. Click 'RUN' to check the attendance by three options: by real-time webcam,\n"
                                  "   recoreded video or given set of images.\n\n",
                  fg = 'black', bg = '#D9E3DA', justify=LEFT).pack(fill = 'y')


    bottom_frame = tkinter.Frame(window2).pack(side = "bottom")



    def train():
        print('train')
        window2.destroy()
        show_train()

    def test():
        print('test')
        window2.destroy()
        show_test()

    def create():
        print('create')
        window2.destroy()
        show_create()

    def run():
        print('run')
        window2.destroy()
        show_run()


    btn1 = tkinter.Button(bottom_frame, text = "TRAIN", fg = "black", bg = '#F2D388', command = train)
    btn1.place(x=230, y=350, width=50)

    btn2 = tkinter.Button(bottom_frame, text = "TEST", fg = "black", bg = '#F2D388', command = test)
    btn2.place(x=330, y=350, width=50)

    btn3 = tkinter.Button(bottom_frame, text = "CREATE", fg = "black", bg = '#F2D388', command = create)
    btn3.place(x=430, y=350, width=50)

    btn3 = tkinter.Button(bottom_frame, text = "RUN", fg = "black", bg = '#F2D388', command = run)
    btn3.place(x=530, y=350, width=50)

    btn4 = tkinter.Button(bottom_frame, text = "EXIT", fg = "red", bg = '#F2D388', command = s_exit)
    btn4.place(x=370, y=450, width=60)

    window2.mainloop()



def show_run():

    window3 = Tk()
    #window3.configure(background='lightyellow')
    window3.title("Smart Attendance System")
    window3.geometry("1200x800")
    tkinter.Label(window3, text = "Smart Attendance System", fg="black", bg="darkorange").pack(fill="x")
    tkinter.Label(window3, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg='orange').pack(fill='x')
    tkinter.Label(window3, text="\n\n ").pack(fill='y')

    #path1 = tk.StringVar()

    tkinter.Label(window3, text = "Enter the path to classifier.pkl").place(x=50, y=50, width=250)
    path1 = tkinter.Entry(window3)
    path1.place(x=60, y=70, width=400)

    tkinter.Label(window3, text = "Enter the path to 20180402-114759 FOLDER").place(x=50, y=100, width=300)
    path2 = tkinter.Entry(window3)
    path2.place(x=60, y=120, width=400)

    tkinter.Label(window3, text = "Enter desired face width and height for face alignment (W*H)").place(x=50, y=150, width=440)
    face_dim = tkinter.Entry(window3)
    face_dim.place(x=60, y=170, width=400)

    tkinter.Label(window3, text = "Enter the gpu memory fraction u want to allocate out of 1").place(x=50, y=200, width=420)
    gpu = tkinter.Entry(window3)
    gpu.place(x=60, y=220, width=400)

    tkinter.Label(window3, text = "Enter the threshold to consider detection by MTCNN").place(x=50, y=250, width=380)
    thresh1 = tkinter.Entry(window3)
    thresh1.place(x=60, y=270, width=400)

    tkinter.Label(window3, text = "Enter the threshold to consider face is recognised").place(x=50, y=300, width=380)
    thresh2 = tkinter.Entry(window3)
    thresh2.place(x=60, y=320, width=400)

    tkinter.Label(window3, text="Default values would be assigned to empyt fields", fg="navy", bg="lightblue").place(x=700, y=200, width=380)
    tkinter.Label(window3, bg = 'orange')
    #Label.place(y = 350, width = 1400)

    rdbtn1 = IntVar()
    rdbtn2 = IntVar()
    rdbtn3 = IntVar()

    rdbi = tkinter.Checkbutton(window3, text="Input: Image", variable = rdbtn3, fg="black", bg="#BFD0CA")
    rdbi.place(x=60, y=400, width=200)

    #tkinter.Label(window3, text="Input: Image", fg="blue", bg="cyan").place(x=60, y=400, width=200)
    tkinter.Label(window3, text = "Enter the folder path inside which images are kept").place(x=300, y=400, width=360)
    img_path = tkinter.Entry(window3)
    img_path.place(x=300, y=420, width=400)

    tkinter.Label(window3, text = "Enter folder path inside which output images are to be saved").place(x=720, y=400, width=420)
    out_img_path = tkinter.Entry(window3)
    out_img_path.place(x=720, y=420, width=400)

    rdbv = tkinter.Checkbutton(window3, text="Input: Video", variable = rdbtn2, fg="black", bg="#BFD0CA")
    rdbv.place(x=60, y=450, width=200)

    #tkinter.Label(window3, text="Input: Video", fg="blue", bg="cyan").place(x=60, y=450, width=200)
    tkinter.Label(window3, text = "Enter path to the video file").place(x=300, y=450, width=200)
    vid_path = tkinter.Entry(window3)
    vid_path.place(x=300, y=470, width=400)

    tkinter.Label(window3, text = "To Save output video type 'y'").place(x=720, y=450, width=200)
    vid_save = tkinter.Entry(window3)
    vid_save.place(x=720, y=470, width=100)

    tkinter.Label(window3, text = "To See output video type y").place(x=950, y=450, width=200)
    vid_see = tkinter.Entry(window3)
    vid_see.place(x=960, y=470, width=100)

    rdbw = tkinter.Checkbutton(window3, text="Input: Webcam", variable = rdbtn1, fg="black", bg="#BFD0CA")
    rdbw.place(x=60, y=500, width=200)
    tkinter.Label(window3, text = "Enter your supported webcam resolution (H*W)").place(x=300, y=500, width=380)
    resolution = tkinter.Entry(window3)
    resolution.place(x=300, y=520, width=400)

    #parameters = path1, path2, face_dim, gpu, thresh1, thresh2, resolution


    def submit():
        print('submit')
        if rdbtn1.get():
            print('Webcam')
            mode = 'w'
        elif rdbtn2.get():
            print('Video')
            mode = 'v'
        elif rdbtn3.get():
            print('Image')
            mode = 'i'
        else:
            print('default')
            mode = 'w'

        print(mode)
        parameters = path1.get(), path2.get(), face_dim.get(), gpu.get(), thresh1.get(), thresh2.get(), resolution.get(), \
                     img_path.get(), out_img_path.get(), vid_path.get(), vid_save.get(), vid_see.get()
        print(parameters)
        #mode = 'w'
        st_name = final_sotware.recognize(mode, parameters)
        print('students recognised', st_name)

    def mark_attend():
        if rdbtn1.get():
            print('Webcam')
            mode = 'w'
        elif rdbtn2.get():
            print('Video')
            mode = 'v'
        elif rdbtn3.get():
            print('Image')
            mode = 'i'
        else:
            print('default')
            mode = 'w'

        print(mode)
        parameters = path1.get(), path2.get(), face_dim.get(), gpu.get(), thresh1.get(), thresh2.get(), resolution.get(), \
                     img_path.get(), out_img_path.get(), vid_path.get(), vid_save.get(), vid_see.get()
        run_attend(mode, parameters)

    btn9 = tkinter.Button(window3, text = "CONTINUE", fg = "black", bg = '#F2D388', command = submit)
    btn9.place(x=550, y=600, width=90)

    btn11 = tkinter.Button(window3, text = "Mark Attendance", fg = "black", bg = '#F2D388', command = mark_attend)
    btn11.place(x=635, y=630, width=120)

    btn10 = tkinter.Button(window3, text = "EXIT", fg = "red", bg = '#F2D388', command = s_exit)
    btn10.place(x=750, y=600, width=60)

    def home():
        window3.destroy()
        gotohome()

    btn12 = tkinter.Button(window3, text = "HOME", fg = "black", bg = '#F2D388', command = home)
    btn12.place(x=650, y=600, width=90)



    window3.mainloop()

def run_attend(mode, parameters):
    present = final_sotware.recognize(mode, parameters)


def show_create():

    window4 = Tk()
    window4.title("Smart Attendance System")
    window4.geometry("800x500")
    tkinter.Label(window4, text = "Smart Attendance System", fg="black", bg="#FBC396").pack(fill="x")
    tkinter.Label(window4, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg='#FBC396').pack(fill='x')
    tkinter.Label(window4, text="\n\n ").pack(fill='y')

    tkinter.Label(window4, text = "Enter the path to output folder").place(x=50, y=50, width=240)
    path1 = tkinter.Entry(window4)
    path1.place(x=60, y=70, width=400)

    tkinter.Label(window4, text = "Enter your supported webcam resolution (eg 640x480)").place(x=50, y=100, width=380)
    webcam = tkinter.Entry(window4)
    webcam.place(x=60, y=120, width=400)

    tkinter.Label(window4, text = "Enter the gpu memory fraction u want to allocate(out of 1)").place(x=50, y=150, width=430)
    gpu = tkinter.Entry(window4)
    gpu.place(x=60, y=170, width=400)

    tkinter.Label(window4, text = "Enter desired face width and height (WidthxHeight format)").place(x=50, y=200, width=430)
    face_dim = tkinter.Entry(window4)
    face_dim.place(x=60, y=220, width=400)

    tkinter.Label(window4, text = "Enter user name (default: person)").place(x=50, y=250, width=260)
    username = tkinter.Entry(window4)
    username.place(x=60, y=270, width=400)

    tkinter.Label(window4, text = "Create dataset using:").place(x=50, y=300, width=180)

    rdbtn1 = IntVar()
    rdbtn2 = IntVar()

    rdbv = tkinter.Checkbutton(window4, text="Video", variable = rdbtn1, fg="black", bg="#BFD0CA")
    rdbv.place(x=220, y=300, width=80)

    rdbw = tkinter.Checkbutton(window4, text="Webcam", variable = rdbtn2, fg="black", bg="#BFD0CA")
    rdbw.place(x=320, y=300, width=80)

    tkinter.Label(window4, text = "Enter video path (if applicable)").place(x=50, y=330, width=250)
    vid_path = tkinter.Entry(window4)
    vid_path.place(x=60, y=350, width=400)

    tkinter.Label(window4, text="Default values would be assigned to empyt fields", fg="navy", bg="lightblue").place(x=50, y=450, width=380)

    tkinter.Label(window4, bg = '#FBC396').place(y = 485, width = 800)

    get_f = 0

    def submit():
        #vid_path2 = ''
        print('submit')
        '''if rdbtn1.get():
            print('Video')
            #vid_path = '/home/aashish/Documents/deep_learning/attendance_deep_learning/scripts_used/video/uri1.webm'
            vid_path2 = vid_path.get()

        elif rdbtn2.get():
            print('Webcam')
            vid_path = ''
        else:
            print('default')
            vid_path = '' '''

        parameters = path1.get(), webcam.get(), face_dim.get(), gpu.get(), username.get(), vid_path.get()
        print(parameters)
        # mode = 'w'
        get_f = final_sotware.dataset_creation(parameters)

        if get_f == 1:
            tkinter.messagebox.showinfo("Attendance", "Dataset Created")


    btn9 = tkinter.Button(window4, text = "CONTINUE", fg = "black", bg = '#F2D388', command = submit)
    btn9.place(x=650, y=200, width=90)

    btn9 = tkinter.Button(window4, text = "EXIT", fg = "red", bg = '#F2D388', command = s_exit)
    btn9.place(x=650, y=300, width=90)

    def home():
        window4.destroy()
        gotohome()

    btn10 = tkinter.Button(window4, text = "HOME", fg = "black", bg = '#F2D388', command = home)
    btn10.place(x=650, y=250, width=90)

    window4.mainloop()



def show_train():

    window5 = Tk()
    window5.title("Smart Attendance System")
    window5.geometry("800x500")
    tkinter.Label(window5, text = "Smart Attendance System", fg="black", bg="#FBC396").pack(fill="x")
    tkinter.Label(window5, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg='#FBC396').pack(fill='x')
    tkinter.Label(window5, text="\n\n ").pack(fill='y')

    tkinter.Label(window5, text = "Enter the path to dataset folder").place(x=50, y=50, width=250)
    path1 = tkinter.Entry(window5)
    path1.place(x=60, y=70, width=400)

    tkinter.Label(window5, text = "Enter the path to 20180402-114759 FOLDER").place(x=50, y=100, width=300)
    path2 = tkinter.Entry(window5)
    path2.place(x=60, y=120, width=400)

    tkinter.Label(window5, text = "Enter the gpu memory fraction u want to allocate(out of 1)").place(x=50, y=150, width=430)
    gpu = tkinter.Entry(window5)
    gpu.place(x=60, y=170, width=400)

    tkinter.Label(window5, text = "Enter the batch size of images to process at once").place(x=50, y=200, width=370)
    batch = tkinter.Entry(window5)
    batch.place(x=60, y=220, width=400)

    tkinter.Label(window5, text = "Enter input image dimension (eg. 160)").place(x=50, y=250, width=285)
    img_dim = tkinter.Entry(window5)
    img_dim.place(x=60, y=270, width=400)

    tkinter.Label(window5, text = "Enter output SVM classifier filename").place(x=50, y=300, width=275)
    svm_name = tkinter.Entry(window5)
    svm_name.place(x=60, y=320, width=400)

    tkinter.Label(window5, text = "Split dataset into training and testing:").place(x=50, y=350, width=305)

    chkbtn1 = IntVar()
    chkbtn2 = IntVar()

    ckbt1 = tkinter.Checkbutton(window5, text="Yes", variable = chkbtn1, fg="black", bg="#BFD0CA")
    ckbt1.place(x=350, y=350, width=50)

    ckbt2 = tkinter.Checkbutton(window5, text="No", variable = chkbtn2, fg="black", bg="#BFD0CA")
    ckbt2.place(x=410, y=350, width=50)

    tkinter.Label(window5, text = "Enter split percentage (if applicable)").place(x=50, y=380, width=290)
    split_percent = tkinter.Entry(window5)
    split_percent.place(x=60, y=400, width=400)

    tkinter.Label(window5, text="Default values would be assigned to empty fields", fg="navy", bg="lightblue").place(x=60, y=450, width=380)

    def submit():

        print('submit')
        if chkbtn1.get():
            print('Yes')
            split_data = 'y'

        elif chkbtn2.get():
            print('No')
            split_data = ''
        else:
            print('default')
            split_data = 'y'

        parameters = path1.get(), path2.get(), batch.get(), img_dim.get(), gpu.get(), svm_name.get(), split_percent.get(), split_data
        print(parameters)
        # mode = 'w'
        get_f = final_sotware.train(parameters)

        if get_f == 1:
            tkinter.messagebox.showinfo("Title", "Training Completed")


    btn9 = tkinter.Button(window5, text = "CONTINUE", fg = "black", bg = '#F2D388', command = submit)
    btn9.place(x=650, y=200, width=90)

    btn9 = tkinter.Button(window5, text = "EXIT", fg = "red", bg = '#F2D388', command = s_exit)
    btn9.place(x=650, y=300, width=90)

    def home():
        window5.destroy()
        gotohome()

    btn10 = tkinter.Button(window5, text = "HOME", fg = "black", bg = '#F2D388', command = home)
    btn10.place(x=650, y=250, width=90)


    window5.mainloop()



def show_test():

    window6 = Tk()
    window6.title("Smart Attendance System")
    window6.geometry("800x500")
    tkinter.Label(window6, text = "Smart Attendance System", fg="black", bg="#FBC396").pack(fill="x")
    tkinter.Label(window6, text = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', bg='#FBC396').pack(fill='x')
    tkinter.Label(window6, text="\n\n ").pack(fill='y')

    tkinter.Label(window6, text = "Enter the path to classifier.pkl").place(x=50, y=50, width=250)
    path1 = tkinter.Entry(window6)
    path1.place(x=60, y=70, width=400)

    tkinter.Label(window6, text = "Enter the path to 20180402-114759 FOLDER").place(x=50, y=100, width=300)
    path2 = tkinter.Entry(window6)
    path2.place(x=60, y=120, width=400)

    tkinter.Label(window6, text="Enter path to dataset folder").place(x=50, y=150, width=230)
    path3 = tkinter.Entry(window6)
    path3.place(x=60, y=170, width=400)

    tkinter.Label(window6, text="Enter the batch size of images to process at once").place(x=50, y=200, width=370)
    batch = tkinter.Entry(window6)
    batch.place(x=60, y=220, width=400)

    tkinter.Label(window6, text="Enter input image dimension (eg. 160)").place(x=50, y=250, width=285)
    img_dim = tkinter.Entry(window6)
    img_dim.place(x=60, y=270, width=400)

    tkinter.Label(window6, text="Default values would be assigned to empyt fields", fg="navy", bg="lightblue").place(x=60, y=450, width=380)

    def submit():

        gpu = 0.8
        parameters = path1.get(), path2.get(), path3.get(), batch.get(), img_dim.get(), gpu
        print(parameters)
        get_f = final_sotware.test(parameters = parameters)

        if get_f == 1:
            tkinter.messagebox.showinfo("Title", "Training Completed")


    btn9 = tkinter.Button(window6, text = "CONTINUE", fg = "black", bg = '#F2D388', command = submit)
    btn9.place(x=650, y=200, width=90)

    btn9 = tkinter.Button(window6, text = "EXIT", fg = "red", bg = '#F2D388', command = s_exit)
    btn9.place(x=650, y=300, width=90)

    def home():
        window6.destroy()
        gotohome()

    btn10 = tkinter.Button(window6, text = "HOME", fg = "black", bg = '#F2D388', command = home)
    btn10.place(x=650, y=250, width=90)



    window6.mainloop()





def gotohome():

  show()
  #show_test()
  #show_train()
  #putwindow()
  #show_run()
  #show_create()

if __name__ == '__main__':
    putwindow()
    #show_attend()
