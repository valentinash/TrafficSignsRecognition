from tkinter import *
from subprocess import call

root = Tk()
root.title('Detektimi i shenjave të trafikut')
root.geometry("500x300")

frame = Frame(root)
frame.pack()

y = 70


def detectFromImg():
    call(["python", "DetectionFromImages.py"])


def detectFromCamera():
    call(["python", "DetectionFromCam.py"])


def detectFromVideo():
    call(["python", "DetectionFromVideo.py"])


btnFromPhotos = Button(root, text="Detektimi\nnga\nfotot", command=detectFromImg,
                       fg="black", font="Verdana 12",
                       bd=2, bg="light blue", relief="raised")
btnFromPhotos.place(x=50, y=y)

btnFromCamera = Button(root, text="Detektimi\nnga\nkamera", command=detectFromCamera,
                       fg="black", font="Verdana 12",
                       bd=2, bg="light blue", relief="raised")
btnFromCamera.place(x=200, y=y)

btnFromVideo = Button(root, text="Detektimi\nnga\nvideo", command=detectFromVideo,
                      fg="black", font="Verdana 12",
                      bd=2, bg="light blue", relief="raised")
btnFromVideo.place(x=350, y=y)

btnClose = Button(root, text="Mbyll", fg="black", font="Verdana 12",
                  bd=2, bg="red", relief="raised", compound=LEFT, command=root.destroy)
btnClose.place(x=220, y=180)

root.mainloop()
