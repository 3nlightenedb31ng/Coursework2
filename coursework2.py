import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
import os
from gtts import gTTS




# Function for existing audio file
def doc():
    f = open('file.txt');
    x = f.read()
    language = 'en'
    audio = gTTS(text=x, lang=language, slow=True)
    audio.save("test.wav")
    os.system("test.wav")



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Alert", "Start Speaking")
        audio = r.listen(source)
        messagebox.showinfo("Alert", "completed.")


    try:
        text = r.recognize_google(audio)
        messagebox.showinfo("Alert", "Converted Text: {}".format(text))
    except:
        messagebox.showerror("ERROR", "Could not recognize the voice")





main_window = tk.Tk()
main_window.geometry('300x300')
main_window.configure(background='red')
main_window.title('Voice Translation')

try:

    btn1 = tk.Button(main_window, text='Audio File', width=25, command=doc)
    btn2 = tk.Button(main_window, text='Start  recording', width=25, command=listen)
    btn3 = tk.Button(main_window,text='Exit',width=25, command=exit)

    btn1.pack(pady=20)
    btn2.pack(pady=20)
    btn3.pack(pady=20)
except:
    messagebox.showinfo("Error", "Something went wrong, please try again")


main_window.mainloop()
