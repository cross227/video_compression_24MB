import subprocess
import os

# user might need to define a different path if a different ffmpeg zip was downloaded
ffmpeg_path = r"C:\ffmpeg-n6.1-latest-win64-lgpl-6.1\bin\ffmpeg.exe"
ffprobe_path = r"C:\ffmpeg-n6.1-latest-win64-lgpl-6.1\bin\ffprobe.exe"

def reduce_video_size(input_file, output_file, target_size_mb=24):
    # Convert target size to bits (1MB = 8,000,000 bits)
    target_size_bits = target_size_mb * 8_000_000

    # Get video duration using ffprobe
    probe_cmd = [ffprobe_path, "-v", "error", "-show_entries", "format=duration", "-of",
                 "default=noprint_wrappers=1:nokey=1", input_file]
    duration = float(subprocess.check_output(probe_cmd).decode().strip())

    # Calculate target bitrate (bits per second)
    target_bitrate = target_size_bits / duration

    # Convert bitrate to kbps
    target_bitrate_kbps = int(target_bitrate / 1000)

    # Run ffmpeg to reduce size and convert to MP4
    ffmpeg_cmd = [
        "C:\\ffmpeg-n6.1-latest-win64-lgpl-6.1\\bin\\ffmpeg.exe",
        "-i", "IMG_4446.MOV",
        "-b:v", "3696k",
        "-c:v", "h264",
        "-preset", "medium",
        "-c:a", "aac",
        "-b:a", "128k",
        "-y", "output_video.mp4"
    ]

    subprocess.run(ffmpeg_cmd, check=True)
    print(f"Video saved as {output_file}, reduced to approximately {target_size_mb}MB")


# input whatever video you want to compress (change the dummy .MOV file to your own)
input_video = "<IMG_0000.MOV>"

#the output generates an .mp4 file and user can change the name
output_video = "<output_video_name>.mp4"
reduce_video_size(input_video, output_video)