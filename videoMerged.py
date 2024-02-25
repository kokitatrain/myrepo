import os
import subprocess

def merge_videos(input_folder, output_file):
    try:
        # Get a list of all video files in the input folder
        video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'))]

        if len(video_files) == 0:
            print("No video files found in the input folder.")
            return

        # Create a text file containing the list of input video files
        with open('filelist.txt', 'w') as filelist:
            for video_file in video_files:
                filelist.write(f"file '{os.path.join(input_folder, video_file)}'\n")

        # Use FFmpeg to merge the videos listed in the text file
        subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', output_file], check=True)

        # Remove the temporary text file
        os.remove('filelist.txt')

        print(f"Merging complete. Merged video saved as: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error while merging videos: {e}")

# Example usage:
input_folder = 'C:/Users/Lenovo/Desktop/A'
output_file = 'C:/Users/Lenovo/Desktop/merged_vido.mp4'
merge_videos(input_folder, output_file)