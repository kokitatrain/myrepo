import os
import subprocess

def convert_dav_folder_to_mp4(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.dav'):
            input_dav_file = os.path.join(input_folder, filename)
            output_mp4_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.mp4')
            
            try:
                subprocess.run(['ffmpeg', '-i', input_dav_file, '-c:v', 'libx264', '-c:a', 'aac', output_mp4_file], check=True)
                print(f"Conversion terminée : {output_mp4_file}")
            except subprocess.CalledProcessError as e:
                print(f"Erreur lors de la conversion : {e}")

# Exemple d'utilisation :
input_folder = 'C:/Users/Lenovo/Desktop/tester'
output_folder = 'C:/Users/Lenovo/Desktop/tesrt'

# Call the function to convert the files
convert_dav_folder_to_mp4(input_folder, output_folder)

