# Hi, I'm Anil Kumar! 👋

## File To Audio Converter
The File To Audio Converter is a Streamlit web application that allows users to convert PDF and DOCX files into audio format. With this tool, users can easily listen to their documents on the go.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/file-to-audio-converter.git`
```
2. Navigate to the project directory:
```bash
cd file-to-audio-converter
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the Streamlit app:
```bash
streamlit run fileToAudio.py
```
2. Open your web browser and go to http://localhost:8501.
3. Upload a PDF or DOCX file using the file uploader.
4. After upload, the app will automatically extract text and convert it to audio.
5. Use the "Preview Audio" button to listen to the audio before downloading.
6. Click "Download Audio" to save the audio file to your device.

## Features
- File Upload: Easily upload PDF or DOCX files for conversion.
- Text Extraction: Automatically extract text from uploaded files.
- Audio Conversion: Convert extracted text to audio (MP3 format).
- Preview Option: Listen to the audio before downloading.
- Direct Download: Download the audio file directly to your device.

## Technologies Used
- `Streamlit`: For building and deploying the web app.
- `pdfplumber`: For extracting text from PDF files.
- `python-docx`: For extracting text from DOCX files.
- `pyttsx3`: For converting text to audio.

## Files Included

- **fileToAudio.py**: This Python script contains the main code for the File To Audio Converter application. It utilizes the Streamlit library for building the user interface, pdfplumber and python-docx for text extraction from PDF and DOCX files, and pyttsx3 for converting text to audio. The script also includes functions for handling file uploads, text-to-audio conversion, and audio file download.

- **requirements.txt**: This file lists all the Python libraries and their versions required for running the File To Audio Converter application. You can install these dependencies using the `pip install -r requirements.txt` command to ensure that the application runs smoothly with all necessary packages.

## Contributing
Contributions are welcome! Please open an issue or create a pull request for any improvements or suggestions.

## Preview
[Checkout Here]()

## 🔗 Follow us
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anilkumarkonathala/)

## Feedback
If you have any feedback, please reach out to us at konathalaanilkumar143@gmail.com