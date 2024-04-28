import streamlit as st
import pdfplumber
import docx
import pyttsx3
import os

st.set_page_config(
    page_title="File To Audio Converter"
)

# Function to convert PDF file to text
def convert_pdf_to_audio(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to convert DOCX file to text
def convert_docx_to_audio(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to convert text to audio
def text_to_audio(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Streamlit app title and file uploader
st.title('File To Audio Converter')
uploaded_file = st.file_uploader("Upload a PDF or DOC file", type=["pdf", "docx"], accept_multiple_files=False)

# Check if file is uploaded
if uploaded_file is not None:
    file_type = uploaded_file.type
    text = ""

    # Convert file based on file type
    if file_type == "application/pdf":
        text = convert_pdf_to_audio(uploaded_file)
    elif file_type.startswith("application/msword") or file_type.startswith("application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
        text = convert_docx_to_audio(uploaded_file)
    else:
        st.error("Unsupported file format. Please upload a PDF or DOCX file.")

    # Display extracted text from uploaded file
    st.write("### Text Extracted from Uploaded File:")
    st.write(text)

    # Set output filename for audio conversion
    output_filename = uploaded_file.name.split('.')[0] + ".mp3"

    # Convert text to audio
    text_to_audio(text, output_filename)

    # Display success message
    st.success("Conversion complete! You can Preview or Download the audio file below.")

    # Preview audio button
    if st.button('Preview Audio'):
        st.audio(output_filename, format="audio/mp3")

    # Download audio button
    with open(output_filename, "rb") as file:
        st.download_button(
            label='Download Audio',
            data=file,
            file_name=output_filename,
            mime="audio/mp3"
        )

    # Remove the generated audio file after download
    os.remove(output_filename)
