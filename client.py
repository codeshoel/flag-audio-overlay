import os
import subprocess
from pydub import AudioSegment
# path = os.path

import ffmpeg


stream = ffmpeg.input('1-001674547782.1_20230124T080943.367Z_1_102.mp3')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'new.mp3')
ffmpeg.run(stream)

# for file in os.scandir("songs"):
#     print(file)
# subprocess.call(["ffmpeg", "1-001674547782.1_20230124T080943.367Z_1_102.mp3", "new_file.wav"])
# # f = AudioSegment.from_mp3("songs/1-001674547782.1_20230124T080943.367Z_1_102.mp3")
# # f.export("con.wav", format="wav")
print("done!")






