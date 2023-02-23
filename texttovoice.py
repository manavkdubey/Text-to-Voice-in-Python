from gtts import gTTS
import os
text1="Hello This is a sample speech"
output=gTTS(text=text1,lang='en',slow=False)
output.save('output.mp3')
os.system("start output.mp3")