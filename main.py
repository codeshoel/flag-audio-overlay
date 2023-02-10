from pydub import AudioSegment
import os
import shutil
from datetime import datetime



class AudioMerge:

    track_1 = None
    track_2 = None


    peers_parent = []
    peers = []

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, error_dir="error_files", output_dir="overlayed_files", original_files_dir="initial_files"):
        
        """"
        The constructor checks the system for essential directories existance, 
        if check returns True the system ignore creating the existing directory.
        if check returns False the system creates the missing directory. 
        """
        
        self.overlayed_files_dir = output_dir
        self.error_files_dir = error_dir
        self.original_files_dir = original_files_dir

        if not os.path.exists(self.error_files_dir):
            os.mkdir(self.error_files_dir)

        if not os.path.exists(self.overlayed_files_dir):
            os.mkdir(self.overlayed_files_dir)

        if not os.path.exists(self.original_files_dir):
            os.mkdir(self.original_files_dir)

    def overlay_multiple(self, dir, *args, **kwargs):
        """
        dir -> Directory where the audio files are stored.
        output_dir -> Directory where the overlayed files are output.
        """
        # date = datetime.now()
        # date_time = str(date).replace(' ', '_').replace(':', '-').replace('.', '_')

        files = os.listdir(dir)

        if len(files) != 1:
            for index in range(1, len(files)):
                
                if len(self.peers) < 2 and files[index] not in self.peers:
                    self.peers.append(files[index])

            for _ in range(1, len(self.peers)):
                audio_1 = self.peers[0]
                audio_2 = self.peers[1]
                
                if audio_1 and audio_2 is not None:

                    # if audio_1 file has no stream or has 0kb move to error_files
                    if os.path.getsize('{}/{}'.format(dir, audio_1)) <= 0:
                        shutil.move("{:s}/{:s}".format(dir, audio_1), "{:s}/{:s}".format(self.error_files_dir, audio_1))
                        self.peers.remove(audio_1)
                    
                        # if audio_2 file has no stream or has 0kb move to error_files
                        if os.path.getsize('{}/{}'.format(dir, audio_2)) <= 0:
                            shutil.move("{:s}/{:s}".format(dir, audio_2), "{:s}/{:s}".format(self.error_files_dir, audio_2))
                            self.peers.remove(audio_2)

                    if str(audio_1).startswith(audio_1[0:15]) == str(audio_2).startswith(audio_1[0:15]):
                        title_format = audio_1.split('_')
                        file_title = "{:s}_{:s}_{:s}".format(title_format[1], title_format[0], title_format[2])
                        try:

                            self.track_1 = AudioSegment.from_file("./{:s}/{:s}".format(dir, audio_1), format="mp3")
                            self.track_2 = AudioSegment.from_file("./{:s}/{:s}".format(dir, audio_2), format="mp3")
                            overlay_track = self.track_1.overlay(self.track_2, position=0)

                            # Export overlayed file to overlayed_files dir
                            overlay_track.export("{:s}/{:s}".format(self.overlayed_files_dir, file_title), format="mp3")
                            
                            shutil.move("{:s}/{:s}".format(dir, audio_1), "{:s}/{:s}".format(self.original_files_dir, audio_1))
                            shutil.move("{:s}/{:s}".format(dir, audio_2), "{:s}/{:s}".format(self.original_files_dir, audio_2))
                            
                            # clear list data when file overlay is complete.
                            self.peers.clear()
                        except Exception as e:
                            return (e.add_note("Error, There was an error while perfoming overlay action,\n error file(s) are moved to ./error_file/."))

                    else:
                        # Moves none-unique file into the error file directory.
                        shutil.move("{:s}/{:s}".format(dir, audio_1), "{:s}/{:s}".format(self.error_files_dir, audio_1))
                        self.peers.clear()
                        return (f"Files with Unique ID are not peerable.[{audio_1} <=> {audio_2}]")
        else:
            # Moves none-unique file into the error file directory.
            shutil.move("{:s}/{:s}".format(dir, files[0]), "{:s}/{:s}".format(self.error_files_dir, files[0]))



if __name__ == '__main__':
    overlay_track = AudioMerge()
    if len(os.listdir('files')) != 0:
        while len(os.listdir('files')) > 0:
            overlay_track.overlay_multiple(dir="files")

        print("Done..!")
    print("File directory is empty.")