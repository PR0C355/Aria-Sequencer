# Aria-Sequencer

This Python application utilizes OpenCV and FFmpeg to convert exported images and audio files from Meta's Project Aria into videos. 

## Requirements

To use this application, you must have the following installed:

-   Python 3
-   OpenCV 4.5.1 or higher
-   FFmpeg 4.2.2 or higher

## Installation

1.  Clone the repository:

`git clone https://github.com/PR0C355/Aria-Sequencer.git`

2.  Install the required packages:

`pip install -r requirements.txt`

## Usage

To use this application, follow these steps:

#### Converting an Image Folder to a Video
1.  Export the images and audio files from Meta's Project Aria.
2.  In the project directory, open the application:  `python main.py`
3.  Click **"Sequence Images"**
4.  Select the folders containing the exported images and the audio file.
5.  Enter the desired video settings, including the output file location, frame rate, and video extension.
6.  Click the "Create Video" button to generate the video.

#### Turning an Exported Folder to Multiple Videos
1.  Export the images and audio files from Meta's Project Aria.
2.  In the project directory, open the application:  `python main.py`
3.  Click **"Sequence Exported Folder"**
4.  Select the folder exported by the Project Aria partner app
5.  Enter the desired video settings, including the output folder location, video extension, and the recording profile used to initially record.
6.  Click the "Process Folder" button to generate the video.

## Installing FFmpeg on Mac

### Step 1: Install Homebrew

The easiest way to install FFmpeg on a Mac is with Homebrew. If you don't have Homebrew installed already, you can install it by running the following command:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`


### Step 2: Install FFmpeg

Once you have Homebrew installed, you can install FFmpeg by running the following command:

Copy code

`brew install ffmpeg`

And that's it! FFmpeg should now be installed on your Mac.

## Installing FFmpeg on Windows

### Step 1: Download the FFmpeg binaries

To install FFmpeg on Windows, you will need to download the FFmpeg binaries from the official FFmpeg website. You can download the binaries from the following link: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

Choose the latest static build for your Windows version (32-bit or 64-bit).

### Step 2: Extract the binaries

Once you have downloaded the FFmpeg binaries, extract them to a location of your choice.

### Step 3: Add FFmpeg to your PATH

To use FFmpeg from the command prompt, you will need to add the location of the FFmpeg binaries to your system's PATH environment variable. To do this, follow these steps:

1.  Open the Start menu and search for "Environment Variables".
2.  Click on "Edit the system environment variables".
3.  Click on the "Environment Variables" button.
4.  Under "System Variables", scroll down and find the "Path" variable.
5.  Click "Edit" and then "New".
6.  Add the location of the FFmpeg binaries that you extracted earlier.

Once you have added FFmpeg to your PATH, you should be able to use it from the command prompt.

That's it! You should now have FFmpeg installed on your Windows machine.


## Supported Formats

-   Input Image Formats: JPEG
-   Input Audio Formats: WAV
-   Output Video Formats: MP4, AVI, MOV, WMV

## Credits

-   OpenCV - [https://opencv.org/](https://opencv.org/)
-   FFmpeg - [https://ffmpeg.org/](https://ffmpeg.org/)

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

If you have any questions or suggestions, please contact tumi.oguntola@gmail.com.