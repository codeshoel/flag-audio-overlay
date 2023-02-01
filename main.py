from pydub import AudioSegment



class AudioMerge:

    track_1 = None
    track_2 = None

    def __init__(self, song_one=None, song_two=None):
        self.track_one = song_one
        self.track_two = song_two

        

        if self.track_one and self.track_two == None:
            return "You have no tracks available for merge."

    def merge_overlay_tracks(self):
        self.track_1 = AudioSegment.from_file("./songs/{:s}".format(self.track_one), format="mp3")
        self.track_2 = AudioSegment.from_file("./songs/{:s}".format(self.track_two), format="mp3")

        # louder = self.track_1 + 6


        overlay_track = self.track_1.overlay(self.track_2, position=0)
        return overlay_track.export("overlayed.mp3", format="mp3")



# C:\Users\USER\Documents\resp\InterraNetwork\audiomerge\songs
# track-2.wav
overlay_track = AudioMerge("1-001674547782.1_20230124T080943.367Z_1_102.mp3", "1-001674547782.1_20230124T080955.260Z_07032031620.mp3")
overlay_track.merge_overlay_tracks()
