from ast import arg
import cv2
import numpy as np
import glob
import ffmpeg
from ffprobe import FFProbe
import tkinter as tk
from tkinter import filedialog
import os
from timeit import default_timer as Timer

def second_time_convert(seconds: float, text: bool = False):
    seconds = round(seconds, 1)
    if seconds < 60:
        if text:
            return f"{seconds} seconds"
        else:
            return f"{seconds}s"
        
    elif seconds < 3600:    
        minutes: int = seconds // 60
        seconds %= 60
        seconds = round(seconds, 1)
        if text:
            return f"{int(minutes)} minutes and {seconds} seconds"
        else:
            return f"{int(minutes)}m {seconds}s"
    elif seconds < 86400:
        seconds = round(seconds)
        hours: int = seconds // 3600
        seconds %= 3600
        seconds = round(seconds, 1)
        minutes = seconds // 60
        seconds %= 60
        if text:
            return f"{int(hours)} hours, {int(minutes)} minutes and {seconds} seconds"
        else:
            return f"{int(hours)}H {int(minutes)}m {seconds}s"
    else:
        seconds = round(seconds)
        days = seconds // 86400
        seconds %= 86400
        seconds = round(seconds, 1)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if text:
            return f"{days} days, {int(hours)} hours, {int(minutes)} minutes and {seconds} seconds"
        else:
            return f"{days}D {int(hours)}H {int(minutes)}m {seconds}s"

    

def create_video(dir: str, output_dir: str = "", video_filename: str = "", aud_dir: str = "", vid_ext: str = "mp4", img_ext: str = "jpg", frame_size: str = "", rotate_clockwise: bool = False, frame_rate: int = 30, status_var: tk.StringVar = None, gui_root: tk.Tk = None):
    create_video_timer = Timer()
    if dir == "":
        return None
    
    if output_dir != "":
        output_dir = f"{output_dir}/"

    images: list[str] = sorted(glob.glob(f'{dir}/*.{img_ext}'))
    
    if frame_size == "":
        dimensions: tuple[int, int] = (cv2.imread(images[0]).shape[0:2])
        print(dimensions)
        print(f"Frame Size: {dimensions[1]}x{dimensions[0]} \n")

    if rotate_clockwise:
        frameSize: tuple[int, int] = (dimensions[0], dimensions[1])
    else:
        frameSize: tuple[int, int] = (dimensions[1], dimensions[0])

    
    print(f"Sequencing Video with images from {dir}")
    if status_var != None:
        status_var.set(f"Sequencing Video with images from {dir}")
        gui_root.update()



    if vid_ext == "mov": #Correct Codec
        codec = "mp4v"

    elif vid_ext == "mp4": #Correct codec
        codec = "mp4v"

    elif vid_ext == "avi": #Correct codec
        codec = "FMP4"

    elif vid_ext == "m4v": #Correct codec
        codec = "mp4v"
    else: 
        vid_ext = "mp4"
        codec = "mp4v"

    if video_filename == "":
        video_filename = dir


    video_output = cv2.VideoWriter(f'{output_dir}{video_filename}-no-audio.{vid_ext}',cv2.VideoWriter_fourcc(*codec), frame_rate, frameSize)
    image_sequence_count = 0
    if rotate_clockwise:
        for filename in images:
            image = cv2.rotate(cv2.imread(filename), cv2.ROTATE_90_CLOCKWISE)
            video_output.write(image)
            print(f"Writing {filename} to video...\n{image_sequence_count}/{len(images)}", end='\r')
            if status_var != None:
                status_var.set(f"Writing {filename} to video...\n{image_sequence_count}/{len(images)} Images Sequenced \n Time Elapsed -  {second_time_convert(Timer() - create_video_timer)}")
                gui_root.update()

            image_sequence_count += 1
    else:
        for filename in images:
            image = cv2.imread(filename)
            video_output.write(image)
            print(f"Writing {filename} to video...\n{image_sequence_count}/{len(images)}", end='\r')
            if status_var != None:
                status_var.set(f"Writing {filename} to video...\n{image_sequence_count}/{len(images)} Images Sequenced \n Time Elapsed -  {second_time_convert(Timer() - create_video_timer)}")
                gui_root.update()
            image_sequence_count += 1

    video_output.release()
    if os.path.exists(f'{output_dir}{video_filename}-no-audio.{vid_ext}'):
        overwrite_blanks = " " * (len("Writing " + filename + " to video...") - len(f"Video Sequencing Complete. {image_sequence_count} image(s) converted to video."))
        print(f"Video Sequencing Complete. {image_sequence_count} image(s) converted to video. {overwrite_blanks} \n")
        if status_var != None:
            status_var.set(f"Video Sequencing Complete. {image_sequence_count} image(s) converted to video. \n Time Elapsed -  {second_time_convert(Timer() - create_video_timer)}")
            gui_root.update()
    else:
        print(f"Vide Sequencing Failed. {overwrite_blanks} \n")
        if status_var != None:
            status_var.set(f"Video Sequencing Failed. \n Time Elapsed -  {second_time_convert(Timer() - create_video_timer)}")
            gui_root.update()
    
    
    if (aud_dir) != "":
        
        print("Adding Audio to Generated Video...", end='\r')
        if status_var != None:
            status_var.set(f"Adding Audio to Generated Video... \n Time Elapsed -  {second_time_convert(Timer() - create_video_timer)}")
            gui_root.update()
        input_vid = ffmpeg.input(f'{output_dir}{video_filename}-no-audio.{vid_ext}')
        input_aud = ffmpeg.input(aud_dir)

        bit_rate = FFProbe(f'{output_dir}{video_filename}-no-audio.{vid_ext}').streams[0].bit_rate


        arg_dict = {"loglevel": "quiet", "stats": None, 'audio_bitrate': f"{str(round(int(bit_rate)/1000))}k"}
        ffmpeg_merger = ffmpeg.output(input_vid, input_aud, f"{output_dir}{video_filename}-audio.{vid_ext}",**arg_dict)

        starting_time = Timer()
        process = ffmpeg_merger.run_async()

        while process.poll() is None:
            print("Adding Audio to Generated Video...", end='\r')
            if status_var != None:
                status_var.set(f"Adding Audio to Generated Video... \n Time Elapsed -  {second_time_convert(Timer() - create_video_timer)}")
                gui_root.update()

        print("Audio Added to Generated Video. \n")
        if status_var != None:
            status_var.set(f"Audio Added to Generated Video. \n Time Elapsed -  {second_time_convert(Timer() - create_video_timer)}")
            gui_root.update()
    
    if os.path.exists(f'{output_dir}{video_filename}-no-audio.{vid_ext}') and os.path.exists(f'{output_dir}{video_filename}-audio.{vid_ext}'):
        print("Video Sequencing Process Complete. \n")
        if status_var != None:
            status_var.set(f"Video Sequencing Process Complete. \n Total Duration: {second_time_convert(Timer() - create_video_timer, True)}")
            gui_root.update()

def video_folder_extraction(dir: str, vid_ext:str, recording_profile: int = 15, status_var: tk.StringVar = None, gui_root: tk.Tk = None, output_dir: str = ""):
    if (dir ==  ""):
        return None

    if recording_profile == 15: # Recording Profile 15
        audio_file = f'{dir}/231-1/{os.listdir(dir + "/231-1/")[0]}'
    
        ArianeRGB = f"{dir}/214-1"
        ArianeSLAM_Left = f"{dir}/1201-1"
        ArianeSLAM_Right = f"{dir}/1201-2"
        ArianeEyeCam = f"{dir}/211-1"

        print("Creating Video for Ariane - RGB Camera...")
        if status_var != None:
            status_var.set("Creating Video for Ariane - RGB Camera...")
            gui_root.update()
        create_video(dir=ArianeRGB, aud_dir=audio_file, rotate_clockwise=True, frame_rate=30, vid_ext=vid_ext, video_filename="Ariane-RGB", output_dir=output_dir, status_var=status_var, gui_root=gui_root)
        print("Video for Ariane - RGB Camera created.")
        if status_var != None:
            status_var.set("Video for Ariane - RGB Camera created.")
            gui_root.update()

        print("Creating Video for Ariane - Left SLAM Camera...")
        if status_var != None:
            status_var.set("Creating Video for Ariane - Left SLAM Camera...")
            gui_root.update()
        create_video(dir=ArianeSLAM_Left, aud_dir=audio_file, rotate_clockwise=True, frame_rate=30, vid_ext=vid_ext, video_filename="Ariane-SLAM_L", output_dir=output_dir, status_var=status_var, gui_root=gui_root)
        print("Video for Ariane - Left SLAM Camera created.")
        if status_var != None:
            status_var.set("Video for Ariane - Left SLAM Camera created.")
            gui_root.update()

        print("Creating Video for Ariane - Right SLAM Camera...")
        if status_var != None:
            status_var.set("Creating Video for Ariane - Right SLAM Camera...")
            gui_root.update()
        create_video(dir=ArianeSLAM_Right, aud_dir=audio_file, rotate_clockwise=True, frame_rate=30, vid_ext=vid_ext, video_filename="Ariane-SLAM_R", output_dir=output_dir, status_var=status_var, gui_root=gui_root)
        print("Video for Ariane - Right SLAM Camera created.")
        if status_var != None:
            status_var.set("Video for Ariane - Right SLAM Camera created.")
            gui_root.update()

        print("Creating Video for Ariane - Eye Camera...")
        status_var.set("Creating Video for Ariane - Eye Camera...")
        gui_root.update()
        create_video(dir=ArianeEyeCam, aud_dir=audio_file, rotate_clockwise=False, frame_rate=10, vid_ext=vid_ext, video_filename="EYE-CAM", output_dir=output_dir, status_var=status_var, gui_root=gui_root)
        print("Video for Ariane - Eye Camera created.")
        if status_var != None:
            status_var.set("Video for Ariane - Eye Camera created.")
            gui_root.update()

        print("Folder Processing Complete.")
        if status_var != None:
            status_var.set("Folder Processing Complete.")
            gui_root.update()
    
# root = tk.Tk()
# root.withdraw()

"""
create_video(dir=filedialog.askdirectory(),
                aud_dir=filedialog.askopenfilename(), 
                vid_ext="m4v", 
                img_ext="jpg", 
                rotate_clockwise=True, 
                frame_rate=10)
"""

# video_folder_extraction(dir=filedialog.askdirectory())