from tkinter import *
from tkinter import filedialog
import os
import imageHandling
import preprocessing


csv_data = []
video_data = []

# Create tk window
win = Tk()
win.geometry("750x550")
win.title("Unity Coordinates Heatmap")

def run():
    if (len(csv_data) >= 1) and (len(video_data) >= 1):
       csv_path = csv_data[0]
       img_path = video_data[0]
       img_length = imageHandling.get_specs(img_path)[0]
       preprocessing.reformat(csv_path, 2, img_length)
       name = csv_path.split("/")[-1]
       name = name[:-4] + "_heatmap"
       imageHandling.analyze_image(img_path, 'temp.csv', name)
       os.remove('temp.csv')
       exit()


def open_csv():
    types = [('csv files', '*.csv')]
    file = filedialog.askopenfile(mode='r', filetypes=types)
    if file:
        csv_path = str(os.path.abspath(file.name))
        Label(win, text="Input Data : " + csv_path, font=('Helvetica 14')).pack()
        csv_data.append(csv_path)


def open_vid():
    #types = [('video files', '*.mp4')]
    types = [('image files', '*.png')]
    file = filedialog.askopenfile(mode='r', filetypes=types)
    if file:
        img_path = str(os.path.abspath(file.name))
        Label(win, text="Input Image : " + img_path, font=('Helvetica 14')).pack()
        video_data.append(img_path)

# Label and buttons
Label(win, text="Import image and coordinate data", font=('Helvetica 14 bold')).pack(pady=20)

Button(win, text="Load .csv", command=open_csv).pack(pady=10)
Button(win, text="Load .png", command=open_vid).pack(pady=10)
Button(win, text="Run", command=run).pack(pady=10)


win.mainloop()



