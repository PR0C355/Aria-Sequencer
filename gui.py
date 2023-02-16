import tkinter as tk
import tkinter.filedialog as fd
import tkinter.font as font
from tkinter import *
from PIL import ImageTk, Image

import Sequencer

BLACK: str = "black"

TITLE_FG: str = "white"
TITLE_BG: str = "black"
LABEL_FG: str = "white"
LABEL_BG: str = "black"
ENTRY_FG: str = "black"
ENTRY_BG: str = "white"


root = tk.Tk()
root.title("Aria Sequencer")
root.geometry("1920x1080")
root.configure(bg=BLACK)


MAIN_MENU_FONT = font.Font(family='Broadway', size=100)
SUBTITLE_FONT = font.Font(family='Broadway', size=25)
STATUS_FONT = font.Font(family='Broadway', size=70)
LARGE_BUTTON_FONT = font.Font(family='Broadway', size=50)


CHOOSE_DIRECTORY_IMAGE = ImageTk.PhotoImage(Image.open("Images/Choose Directory.png", mode='r').resize((200, 100)))

VIDEO_EXTENSIONS = ["mov", "mp4", "avi", "m4v"]
RECORDING_PROFILES = [15]

def main_page():
    global root

    global main_title
    main_title = tk.Label(
        root,
        text = "Aria Sequencer",
        foreground=TITLE_FG,
        background=TITLE_BG,
        font=MAIN_MENU_FONT
    )

    global video_creation_button
    video_creation_button = tk.Button(
        root,
        text = "Folder to Video",
        font = SUBTITLE_FONT,
        bg = "#63666A",
        fg = "black",
        command = main_to_video_creator,
    )

    global folder_processor_button
    folder_processor_button = tk.Button(
        root,
        text = "Convert Exported Folder to Multiple Streams",
        font = SUBTITLE_FONT,
        bg = "#63666A",
        fg = "black",
        command = main_to_folder_processor,
    )

    main_title.pack()
    video_creation_button.pack()
    folder_processor_button.pack()

def video_creator():
    global selected_image_directory
    selected_image_directory = tk.StringVar(root)
    selected_image_directory.set("~")

    global selected_video_filename
    selected_video_filename = tk.StringVar(root)
    selected_video_filename.set("")

    global selected_audio_file
    selected_audio_file = tk.StringVar(root)
    selected_audio_file.set("")

    global selected_video_extension
    selected_video_extension = tk.StringVar(root)
    selected_video_extension.set("mp4")

    global selected_clockwise
    selected_clockwise = tk.BooleanVar(root)
    selected_clockwise.set(False)

    global selected_frame_rate
    selected_frame_rate = tk.IntVar(root)
    selected_frame_rate.set(30)

    global selected_output_directory
    selected_output_directory = tk.StringVar(root)
    selected_output_directory.set("")

    global download_status
    download_status = tk.StringVar(root)
    download_status.set("")


    # Image Directory
    global image_directory_frame
    global selected_image_directory_label
    global selected_image_directory_entry
    global download_directory_button

    image_directory_frame = tk.Frame(root, bg=BLACK)
    image_directory_frame.pack()

    selected_image_directory_label = tk.Label(
        image_directory_frame,
        text="Image Directory:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_image_directory_label.pack(side=LEFT)

    selected_image_directory_entry = tk.Entry(
        image_directory_frame,
        textvariable=selected_image_directory,
        width=44,
        font=SUBTITLE_FONT,
        bg=ENTRY_BG,
        fg=ENTRY_FG,
    )
    selected_image_directory_entry.config(borderwidth=5, highlightthickness=0)
    selected_image_directory_entry.pack(side=LEFT)

    download_directory_button = tk.Button(
        image_directory_frame,
        text = "Choose Directory",
        font = SUBTITLE_FONT,
        borderwidth=0,
        bg = BLACK,
        image=CHOOSE_DIRECTORY_IMAGE,
        command = lambda: selected_image_directory.set(f"{fd.askdirectory()}")
    )
    download_directory_button.pack(side=LEFT) 

    # Video Filename
    global video_filename_frame
    global selected_video_filename_label
    global selected_video_filename_entry
    
    video_filename_frame = tk.Frame(root, bg=BLACK)
    video_filename_frame.pack()

    selected_video_filename_label = tk.Label(
        video_filename_frame,
        text="Video Filename:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_video_filename_label.pack(side=LEFT)
    
    selected_video_filename_entry = tk.Entry(
        video_filename_frame,   
        textvariable=selected_video_filename,
        width=44,
        font=SUBTITLE_FONT,
        bg=ENTRY_BG,
        fg=ENTRY_FG,
    )
    selected_video_filename_entry.config(borderwidth=5, highlightthickness=0)
    selected_video_filename_entry.pack(side=LEFT)

    # Audio File
    global audio_file_frame
    global selected_audio_file_label
    global selected_audio_file_entry
    global selected_audio_file_button

    audio_file_frame = tk.Frame(root, bg=BLACK)
    audio_file_frame.pack()

    selected_audio_file_label = tk.Label(
        audio_file_frame,
        text="Audio File:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_audio_file_label.pack(side=LEFT)

    selected_audio_file_entry = tk.Entry(
        audio_file_frame,
        textvariable=selected_audio_file,
        width=44,
        font=SUBTITLE_FONT,
        bg=ENTRY_BG,
        fg=ENTRY_FG,
    )
    selected_audio_file_entry.config(borderwidth=5, highlightthickness=0)
    selected_audio_file_entry.pack(side=LEFT)

    selected_audio_file_button = tk.Button(
        audio_file_frame,
        text = "Choose File",
        font = SUBTITLE_FONT,
        bg = BLACK,
        # image=CHOOSE_DIRECTORY_IMAGE,
        command = lambda: selected_audio_file.set(f"{fd.askopenfilename()}")
    )   
    selected_audio_file_button.pack(side=LEFT)

    global video_extension_frame
    video_extension_frame = tk.Frame(root)
    video_extension_frame.pack()

    # Video Extension
    global selected_video_extension_label
    global selected_video_extension_entry

    selected_video_extension_label = tk.Label(
        video_extension_frame,
        text="Video Extension:   ",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_video_extension_label.pack(side=LEFT)

    selected_video_extension_entry = tk.OptionMenu(
        video_extension_frame,
        selected_video_extension,
        *VIDEO_EXTENSIONS,
        command = lambda x: selected_video_extension.set(x)
    )
    selected_video_extension_entry.pack(side=LEFT)

    # Clockwise
    global selected_clockwise_button
    global selected_clockwise_entry

    selected_clockwise_button = tk.Checkbutton(
        root,
        text="Turn 90\U000000B0 Clockwise",
        variable=selected_clockwise,
        onvalue=True,
        offvalue=False,
        font=SUBTITLE_FONT,
        bg="black",
        fg="white",
    )
    selected_clockwise_button.pack()

    # Frame Rate
    global frame_rate_frame
    global selected_frame_rate_label
    global selected_frame_rate_entry

    frame_rate_frame = tk.Frame(root, bg=BLACK)
    frame_rate_frame.pack()

    selected_frame_rate_label = tk.Label(
        frame_rate_frame,
        text="Frame Rate:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_frame_rate_label.pack(side=LEFT)

    selected_frame_rate_entry = tk.Entry(
        frame_rate_frame,
        textvariable=selected_frame_rate,
        width=44,
        font=SUBTITLE_FONT,
        bg=ENTRY_BG,
        fg=ENTRY_FG
    )
    selected_frame_rate_entry.config(borderwidth=5, highlightthickness=0)
    selected_frame_rate_entry.pack(side=LEFT)

    # Output Directory
    global selected_output_directory_frame
    global selected_output_directory_label
    global selected_output_directory_entry
    global selected_output_directory_button

    selected_output_directory_frame = tk.Frame(root, bg=BLACK)
    selected_output_directory_frame.pack()

    selected_output_directory_label = tk.Label(
        selected_output_directory_frame,
        text="Output Directory:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_output_directory_label.pack(side=LEFT)

    selected_output_directory_entry = tk.Entry(
        selected_output_directory_frame,
        textvariable=selected_output_directory,
        width=44,
        font=SUBTITLE_FONT,
        bg=ENTRY_BG,
        fg=ENTRY_FG
    )
    selected_output_directory_entry.config(borderwidth=5, highlightthickness=0)
    selected_output_directory_entry.pack(side=LEFT)

    selected_output_directory_button = tk.Button(
        selected_output_directory_frame,
        text = "Choose Directory",
        font = SUBTITLE_FONT,
        bg = BLACK,
        # image=CHOOSE_DIRECTORY_IMAGE,
        command = lambda: selected_output_directory.set(f"{fd.askdirectory()}")
    )
    selected_output_directory_button.pack(side=LEFT)

    # Create Video Button
    global create_video_button
    create_video_button = tk.Button(
        root,
        text = "Create Video",
        font = SUBTITLE_FONT,
        bg = "#63666A",
        fg = "black",
        command = lambda: Sequencer.create_video(dir=selected_image_directory.get(), output_dir=selected_output_directory.get(), video_filename=selected_video_filename.get(), aud_dir=selected_audio_file.get(), vid_ext=selected_video_extension.get(), rotate_clockwise=selected_clockwise.get(), frame_rate=selected_frame_rate.get(), status_var=download_status, gui_root=root)
    )
    create_video_button.pack()

    # Download Status
    global download_status_label
    download_status_label = tk.Label(
        root,
        textvariable=download_status,
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    download_status_label.pack()


    # Back Button
    global back_button
    back_button = tk.Button(
        root,
        text = "Back",
        font = SUBTITLE_FONT,
        bg = "#63666A",
        fg = "black",
        command = video_creator_to_main,
    )
    back_button.pack()

def folder_processor():
    global selected_folder_directory
    selected_folder_directory = tk.StringVar(root)
    selected_folder_directory.set("~")

    global selected_folder_extension
    selected_folder_extension = tk.StringVar(root)
    selected_folder_extension.set("~")

    global selected_folder_recording_profile
    selected_folder_recording_profile = tk.IntVar(root)
    selected_folder_recording_profile.set(15)

    global selected_folder_output_directory
    selected_folder_output_directory = tk.StringVar(root)
    selected_folder_output_directory.set("")

    global download_status
    download_status = tk.StringVar(root)
    download_status.set("")

    # Folder Directory
    global selected_folder_directory_label
    global selected_folder_directory_entry
    global selected_folder_directory_button

    selected_folder_directory_label = tk.Label(
        root,
        text="Select Directory:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_folder_directory_label.pack()

    selected_folder_directory_entry = tk.Entry(
        root,
        textvariable=selected_folder_directory,
        width=44,
        font=SUBTITLE_FONT,
        bg=ENTRY_BG,
        fg=ENTRY_FG
    )
    selected_folder_directory_entry.config(borderwidth=5, highlightthickness=0)
    selected_folder_directory_entry.pack()

    selected_folder_directory_button = tk.Button(
        root,
        text = "Choose Directory",
        font = SUBTITLE_FONT,
        bg = BLACK,
        # image=CHOOSE_DIRECTORY_IMAGE,
        command = lambda: selected_folder_directory.set(f"{fd.askdirectory()}")
    )
    selected_folder_directory_button.pack() 

    # Export Extension
    global selected_export_extension_label
    global selected_export_extension_entry

    selected_export_extension_label = tk.Label(
        root,
        text="Select Extension:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_export_extension_label.pack()
    selected_export_extension_entry = tk.OptionMenu(
        root,
        selected_folder_extension,
        *VIDEO_EXTENSIONS,
        command = lambda x: selected_folder_extension.set(x)
    )
    selected_export_extension_entry.pack() 

    global selected_folder_recording_profile_label
    global selected_folder_recording_profile_entry

    selected_folder_recording_profile_label = tk.Label(
        root,
        text="Select Recording Profile:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_folder_recording_profile_label.pack()
    selected_folder_recording_profile_entry = tk.OptionMenu(
        root,
        selected_folder_recording_profile,
        *RECORDING_PROFILES,
        command = lambda x: selected_folder_recording_profile.set(x)
    )
    selected_folder_recording_profile_entry.pack()

    # Output Directory
    global selected_folder_output_directory_label
    global selected_folder_output_directory_entry
    global selected_folder_output_directory_button

    selected_folder_output_directory_label = tk.Label(
        root,
        text="Select Output Directory:",
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    selected_folder_output_directory_label.pack()

    selected_folder_output_directory_entry = tk.Entry(
        root,
        textvariable=selected_folder_output_directory,
        width=44,
        font=SUBTITLE_FONT,
        bg=ENTRY_BG,
        fg=ENTRY_FG,
    )
    selected_folder_output_directory_entry.config(borderwidth=5, highlightthickness=0)
    selected_folder_output_directory_entry.pack()

    selected_folder_output_directory_button = tk.Button(
        root,
        text = "Choose Directory",
        font = SUBTITLE_FONT,
        bg = BLACK,
        # image=CHOOSE_DIRECTORY_IMAGE,
        command = lambda: selected_folder_output_directory.set(f"{fd.askdirectory()}")
    )
    selected_folder_output_directory_button.pack()

    # Process Folder Button
    global process_folder_button
    process_folder_button = tk.Button(
        root,
        text = "Process Folder",
        font = SUBTITLE_FONT,
        bg = "#63666A",
        fg = "black",
        command = lambda: Sequencer.video_folder_extraction(dir=selected_folder_directory.get(), vid_ext=selected_folder_extension.get(),recording_profile=selected_folder_recording_profile.get(), status_var=download_status, gui_root=root, output_dir=selected_folder_output_directory.get()),
    )
    process_folder_button.pack()

    # Download Status
    global download_status_label
    download_status_label = tk.Label(
        root,
        textvariable=download_status,
        # width=50,
        font=SUBTITLE_FONT,
        background=LABEL_BG,
        fg=LABEL_FG
    )
    download_status_label.pack()

    # Back Button
    global back_button
    back_button = tk.Button(
        root,
        text = "Back",
        font = SUBTITLE_FONT,
        bg = "#63666A",
        fg = "black",
        command = folder_processor_to_main,
    )
    back_button.pack()

def remove_main_page():
    main_title.pack_forget()
    video_creation_button.pack_forget()
    folder_processor_button.pack_forget()

def remove_video_creator():
    image_directory_frame.pack_forget()
    selected_image_directory_label.pack_forget()
    selected_image_directory_entry.pack_forget()
    download_directory_button.pack_forget()
    
    video_filename_frame.pack_forget()
    selected_video_filename_label.pack_forget()
    selected_video_filename_entry.pack_forget()
    
    audio_file_frame.pack_forget()
    selected_audio_file_label.pack_forget()
    selected_audio_file_entry.pack_forget()
    selected_audio_file_button.pack_forget()

    video_extension_frame.pack_forget()
    selected_video_extension_label.pack_forget()
    selected_video_extension_entry.pack_forget()

    selected_clockwise_button.pack_forget()

    frame_rate_frame.pack_forget()
    selected_frame_rate_label.pack_forget()
    selected_frame_rate_entry.pack_forget()

    selected_output_directory_frame.pack_forget()
    selected_output_directory_label.pack_forget()
    selected_output_directory_entry.pack_forget()
    selected_output_directory_button.pack_forget()

    create_video_button.pack_forget()
    download_status_label.pack_forget()
    back_button.pack_forget()

def remove_folder_processor():
    selected_folder_directory_label.pack_forget()
    selected_folder_directory_entry.pack_forget()
    selected_folder_directory_button.pack_forget()
    selected_export_extension_label.pack_forget()
    selected_export_extension_entry.pack_forget()
    selected_folder_recording_profile_label.pack_forget()
    selected_folder_recording_profile_entry.pack_forget()
    selected_folder_output_directory_label.pack_forget()
    selected_folder_output_directory_entry.pack_forget()
    selected_folder_output_directory_button.pack_forget()
    process_folder_button.pack_forget()
    download_status_label.pack_forget()
    back_button.pack_forget() 

def main_to_video_creator():
    remove_main_page()
    video_creator()

def video_creator_to_main():
    remove_video_creator()
    main_page()

def main_to_folder_processor():
    remove_main_page()
    folder_processor()

def folder_processor_to_main():
    remove_folder_processor()
    main_page()
