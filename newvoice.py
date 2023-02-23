from gtts import gTTS
import os
text1=open('demo.txt','r').read()
output=gTTS(text=text1,lang='en',slow=False)
output.save('output1.mp3')
os.system("start output1.mp3")