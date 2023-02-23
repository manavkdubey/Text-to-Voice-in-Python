import tkinter as tk
from gtts import gTTS
import os
def texttospeech(i):
    text1=i
    output=gTTS(text=text1,lang='en',slow=False)
    output.save('output1.mp3')
    os.system("start output1.mp3")

  


window =tk.Tk()
window.title("Conversion Engine") 
window.geometry("700x1100")
input_entry=tk.Entry(window) 
input_label=tk.Label(window,text="Enter your text")

speech_button=tk.Button(window,text="Text to speech",command=lambda:texttospeech(input_entry.get()))
input_label.grid(row=0,column=0)
input_entry.grid(row=0,column=1)
speech_button.grid(row=1,column=1)
window.mainloop()