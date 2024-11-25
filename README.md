# Korivash AMV Manager Tool

Korivash AMV Manager Tool is a simple and user-friendly Python-based application designed to help AMV (Anime Music Video) creators organize their video clips, add audio tracks, and export the final AMV. With an easy-to-use graphical user interface (GUI), you can quickly build an AMV by adding multiple video clips and audio tracks, then export the finished product.

## Features
- **Add Video Clips**: Easily add multiple video clips to create your AMV.
- **Trim Video Clips**: Trim video clips to include only the portions you need.
- **Reorder Video Clips**: Reorder added video clips to structure your AMV as desired.
- **Delete Video Clips**: Delete unwanted video clips from your project.
- **Loop Clips**: Enable looping of video clips if the audio is longer than the available video.
- **Add Background Music**: Import an audio track to be used as background music for your AMV.
- **Trim Audio Track**: Trim the audio track to fit the video clips.
- **Delete Audio Track**: Remove the audio track if needed.
- **Export AMV**: Combine the added clips and audio to export your final AMV in `.mp4` format.
- **Export Audio Only**: Export only the audio in `.mp3` or `.wav` format.
- **Modern Dark-Themed GUI**: The tool has a sleek, dark-themed GUI for a comfortable editing experience.

## Prerequisites
- **Python 3.7+**: Make sure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).
- **pip**: Python's package manager, usually installed with Python.

## Installation
1. Clone this repository or download the code.
   ```sh
   git clone <repository-url>
   cd korivash-amv-manager-tool
   ```
2. Install the required Python packages. Use the following command to install all the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   The `requirements.txt` file should include:
   ```
   moviepy
   tk
   ttkthemes
   ```

## Running the Tool
To run the Korivash AMV Manager Tool, follow these steps:

1. Navigate to the directory containing `main.py`.
   ```sh
   cd korivash-amv-manager-tool
   ```
2. Run the script using Python:
   ```sh
   python main.py
   ```

## File Structure
- **main.py**: Entry point for running the AMV Manager Tool.
- **gui_components.py**: Contains GUI-related components and interface definitions.
- **video_operations.py**: Handles video-related operations such as adding, trimming, deleting, and exporting video clips.
- **audio_operations.py**: Manages audio-related operations including adding, trimming, deleting, and exporting audio files.
- **utils.py**: Contains utility functions used throughout the tool, such as time conversion.
- **start.bat**: Batch file to easily start the tool on Windows systems.

## Using the Tool

1. **Add Video Clips**: Click the "Add Video Clip" button to select video files (`.mp4`, `.avi`, `.mov`) from your system. The added clips will be displayed in the text area.

2. **Add Audio Track**: Click the "Add Audio Track" button to select an audio file (`.mp3`, `.wav`) that will be used as the background music for your AMV.

3. **Trim Video/Audio**: Use the trim options to select the start and end points for both video clips and audio.

4. **Reorder Clips**: Click "Reorder Clips" to change the order of added video clips.

5. **Delete Clips/Audio**: Use the delete buttons to remove video clips or the audio track if needed.

6. **Loop Clips**: If the audio is longer than the video, you can enable the "Loop Clips" option to loop the video clips until the audio ends.

7. **Export AMV**: Once you have added all the desired video clips and an optional audio track, click the "Export AMV" button. Select the location where you want to save the final AMV (`.mp4` format). The export will run in a separate thread to avoid freezing the application.

8. **Export Audio Only**: If you only want to export the audio, click the "Export Audio" button to save it in `.mp3` or `.wav` format.

## Troubleshooting
- **GUI Freezing**: Exporting the AMV runs in a separate thread to prevent the GUI from freezing. If the export takes longer, please be patient.
- **Missing Dependencies**: Make sure to run `pip install -r requirements.txt` to install all necessary libraries before running the tool.
- **File Compatibility**: The tool supports video files in `.mp4`, `.avi`, `.mov` formats and audio files in `.mp3`, `.wav` formats. Make sure your files are in these formats to avoid errors.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Contributions are welcome! If you have suggestions or find a bug, feel free to open an issue or submit a pull request.

## Contact
- **Developer**: Korivash
- **Discord**: [Join my Discord](https://discord.gg/B8v945fjuS)
- **YouTube**: [Watch my latest AMVs](https://youtube.com/Korivash)
- **Twitch**: [See me live on Twitch](https://twitch.tv/Korivash)
