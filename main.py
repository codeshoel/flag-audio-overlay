from pydub import AudioSegment
import os

peers_parent = []
peers = []

# index[13]



class AudioMerge:

    track_1 = None
    track_2 = None


    peers_parent = []
    peers = []

    def __init__(self):
        pass

        

        # if self.track_1 and self.track_2 == None:
        #     return "You have no tracks available for merge."

    def overlay_multiple(self, dir):
        for files in os.scandir(dir):
            self.peers_parent.append(files.name)


        for idx in range(len(self.peers_parent)):
            if (self.peers_parent[idx] not in peers) and (len(self.peers) < 2):
                self.peers.append(self.peers_parent[idx])
    
        audio_1 = self.peers[0]
        audio_2 = self.peers[1]

        self.track_1 = AudioSegment.from_file("./{:s}/{:s}".format(dir, audio_1), format="mp3")
        self.track_2 = AudioSegment.from_file("./{:s}/{:s}".format(dir, audio_2), format="mp3")

        try:
            overlay_track = self.track_1.overlay(self.track_2, position=0)

        except Exception as e:
            return e

        else:
            try:
                overlay_track.export("Inteera-networks-{:s}.mp3".format(audio_1[17:31]), format="mp3")
                print("title 1:", audio_1)
                print("title 2:", audio_2)
            except Exception as e:
                return e
                # pass
            else:
                if (os.path.isfile("./{:s}/{:s}/".format(dir, audio_1)) and os.path.isfile("./{:s}/{:s}/".format(dir, audio_2))):
                    os.remove("./{:s}/{:s}".format(dir, audio_1))
                    os.remove("./{:s}/{:s}".format(dir, audio_2))
                else:
                    print("No such file in specified dir.")


    def merge_overlay_tracks(self):
        pass




overlay_track = AudioMerge()
overlay_track.overlay_multiple("dir_st")
