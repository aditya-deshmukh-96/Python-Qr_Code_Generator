from tkinter import *
from tkinter import messagebox,filedialog
import qrcode
from PIL import ImageTk,Image
import time
import re

def generateqr(url):
  # Using regular expression to check URL
  a = re.search('^https://www.',url) #highlight

  if not a:
    messagebox.showerror('Inavlid URL','Your URL should start with \'https://www.\'')
    return
  # print(a) # debug
  win.geometry('265x430')

  # Generate QR code
  qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 5,
    border = 3
  )

  qr.add_data(url)
  qr.make(fit=True)
  img = qr.make_image(fill_color = 'black',back_color = 'white')
  # img.show()
  # img.save('C:\\Users\\Deshmukh\\Desktop\\my_project\\qrcode_GUI\\images\\qrimg.png')
  lbfr.destroy()
  global myimg  #highlight
  myimg = ImageTk.PhotoImage(img)
  lb = Label(win,image=myimg,padx=30,pady=30,borderwidth=1,relief=SOLID)
  lb.grid(row=0,column=0,padx=50,pady=50)

  btnsave = Button(win,text='Save',padx=15,pady=5,borderwidth=1,relief='solid',command=lambda: save(myimg))
  btnsave.grid(row=4,column=0) 


def save(img):
  
  img = filedialog.asksaveasfile(initialdir='C:\\Users\\Deshmukh\\Desktop\\my_project\\qrcode_GUI\\images', defaultextension=".png",filetypes=[('All Files', '*.*')])
  print(img)
  if img:
    # print(True)
    lblip = Entry(win)
    # lblip.insert(' ')
    lblip.grid(row=2,column=0)
    messagebox.showinfo('Image Status','File saved Successfully!')
    

  else:
    # print(False)
    messagebox.showerror('Image Status','File not saved')

# ------------------------------- main -------------------------------
win = Tk()
win.title('QR Code Generator')
win.geometry('270x270')

lbfr = Label(win,text='qr will be displayed here',padx=20,pady=10,borderwidth=1,relief=SOLID)
lbfr.grid(row=0,column=0,padx=50,pady=50)

lblurl = Label(win,text='Enter URL here:')
lblurl.grid(row=1,column=0)

lblip = Entry(win,width=40)
lblip.grid(row=2,column=0)
lblip.focus()
# lblip.bind("<Return>",generateqr(lblip.get()))

btn = Button(win,text='Generate',borderwidth=1,padx=10,pady=5, relief='solid',command=lambda: generateqr(lblip.get(),))
btn.grid(row=3,column=0,pady=17)
print('Button: ',btn)

win.mainloop()