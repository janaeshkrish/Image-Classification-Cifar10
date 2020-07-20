import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import numpy 
from skimage.transform import resize
from tensorflow.keras.models import load_model

model = load_model('model.h5')

classes = {
    0:"Aeroplane",
    1:"Automobile",
    2:"Bird",
    3:"Cat",
    4:"Deer",
    5:"Dog",
    6:"Frog",
    7:"Horse",
    8:"Ship",
    9:"Truck"
}


def upload_image():
    filepath = filedialog.askopenfilename()
    uploaded = Image.open(filepath)
    uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_width()/2.25)))
    im = ImageTk.PhotoImage(uploaded)
    simage.configure(image=im)
    simage.image = im
    label.configure(text='')
    show_classify_button(filepath)

def show_classify_button(filepath):
    classify_btn = Button(top,text="classify image",command=lambda : classify(filepath),padx=10,pady=5)
    classify_btn.configure(background="#364156",foreground="white",font=('arial',20,'bold'))
    classify_btn.place(relx=0.79,rely=0.46)


def classify(filepath):
    image = Image.open(filepath)
    image = image.resize((32,32))
    image = numpy.expand_dims(image,axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground="#011638",text = sign)


#setting up the GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Image Classifier')
top.configure(background = 'grey')

# set heading
heading = Label(top,text="IMAGE CLASSIFIER",pady=20,font=('arial',20,'bold'))
heading.configure(background = 'grey',foreground='red')
heading.pack()

#set upload button
upload = Button(top,text="Upload image",command = upload_image,padx=10,pady=5)
upload.configure(background = "#364156",foreground="white",font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)

#uploaded image
simage = Label(top)
simage.pack(side=BOTTOM,expand=True)


#predicted class
label = Label(top,background='grey',font=('arial',10,'bold'))
label.pack(side=BOTTOM,expand=True)


top.mainloop()