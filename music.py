import pygame
import os

# Initialize pygame
pygame.init()

# Set the path to your music directory
music_directory = "/path/to/your/music/directory"

# Get a list of all music files in the directory
music_files = [f for f in os.listdir(music_directory) if f.endswith("play.mp3")]

# Initialize the mixer for audio playback
pygame.mixer.init()

# Function to play a selected music file
def play_music(file):
    pygame.mixer.music.load(os.path.join(music_directory, file))
    pygame.mixer.music.play()

# Main loop
while True:
    print("Music Player")
    print("-------------")
    for i, file in enumerate(music_files):
        print(f"{i + 1}. {file}")
    print("Q. Quit")
    
    choice = input("Select a song to play (1-{len(music_files)}) or press Q to quit: ")
    
    if choice.lower() == "q":
        break
    
    try:
        choice = int(choice)
        if 1 <= choice <= len(music_files):
            selected_file = music_files[choice - 1]
            play_music(selected_file)
            input(f"Now playing: {selected_file}. Press Enter to stop.")
            pygame.mixer.music.stop()
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number or Q to quit.")

# Clean up and quit
pygame.mixer.quit()
pygame.quit()
