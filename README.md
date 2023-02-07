## HOW TO INSTALL FLAGE-AUDIO-OVERLAY

- clone this repository:
    `git clone https://github.com/codeshoel/audio-overlay.git`

- Create a virtual environment: 
    `python -m venv <venv_name>`

- Activate the virtual environment:
    - Windows: `<venv_name>\Scripts\activate`
    - Run this command to upgrade pip utilite: `python -m pip install --upgrade pip`

### To Run the Script Smoothly you will need to install ffmpeg on your Operating System
- Download FFmpeg for Windows from: [FFmpeg download page](https://ffmpeg.org/download.html)

    ![Image 1](https://phoenixnap.com/kb/wp-content/uploads/2022/10/choose-build-from-gyan.png)

    - In the git master builds section, search for the latest version of the FFmpeg build and download the full build beacause it has the up-to-date libraries.

    ![Image 2](https://phoenixnap.com/kb/wp-content/uploads/2022/10/downloading-the-full-build.png)

    - Extract the downloaded file using any file unziper utilite e.g `WinRaR, 7-Zip`.

    - Open the extracted folder and rename the child folder within the parent.

    ![Image 3](https://phoenixnap.com/kb/wp-content/uploads/2022/10/renaming-a-file.png)

    - Move or copy the child folder to the root of the C drive or the folder of your choice.
    ![Image 4](https://phoenixnap.com/kb/wp-content/uploads/2022/10/mover-ffmpeg-folder-to-c-drive-1.png)

    ### **Add FFmpeg to PATH**
    - Type system variables into the search bar and click the Edit the system environment variables option.
    ![Image 5](https://phoenixnap.com/kb/wp-content/uploads/2022/10/choose-system-variables.png)

    - Under the User variables section, select Path and click the Edit button.
    ![Image 6](https://phoenixnap.com/kb/wp-content/uploads/2022/10/choose-path.png)

    - Click on New from the side menu.
    ![Image 7](https://phoenixnap.com/kb/wp-content/uploads/2022/10/add-new-variable.png)

    - Add C:\ffmpeg\bin to the empty field and confirm changes with OK
    ![Image 8](https://phoenixnap.com/kb/wp-content/uploads/2022/10/adding-ffmpeg-variable.png)

    - To verify FFmpeg Installation, use any among the commands below
        - Run: `ffmpeg` **OR** `ffmpeg -version`
        
        ![Image 9](https://phoenixnap.com/kb/wp-content/uploads/2022/10/ffmpeg-version-command-prompt-output.png)

### To Run the script
-   Go back to the script folder and create the following directory, you will do these only when setting it up for the first time:
    - folder name: `files`

-   If everything went successfully copy the audio files you wish to merge(overlay) into the `files` directory and run **`main.py`** on the terminal where your virtual environment is activated:
    - `py main.py`

