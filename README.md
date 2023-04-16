
# PDF Text Embeddings & GPT-3.5 Turbo

This is a Python-based repository that allows users to upload PDF files using Streamlit's file uploader, extract the text from each page of the PDF file, generate embeddings for each row using OpenAI's ada-002 model, and answer questions related to the extracted text using the OpenAI GPT-3.5 Turbo model. The extracted text is then displayed in the web page.

## How to Use
1- Clone this repository to your local machine.                    
2- Install the required dependencies using ``` pip install -r requirements.txt```  
3- Run the application using ``` streamlit run app.py ```       
4- Upload your PDF file using the file uploader in the web page.   
5-The extracted text will be displayed on the page along with the embeddings generated using OpenAI's ada-002 model.          
6- You can ask questions related to the extracted text in the text box provided and click on the "Ask" button.     
7-The OpenAI GPT-3.5 Turbo model will be used to generate answers to your questions based on the extracted text. 

## Requirements

- Python 3.x
- streamlit
- textract
- pandas
- numpy
- openai


## Screenshots

![App Screenshot](https://github.com/bileldhambri/PDF-text-embeddings-chatgpt3.5-turbo/blob/main/Screenshots/Interface.PNG?raw=true)
![App Screenshot](https://github.com/bileldhambri/PDF-text-embeddings-chatgpt3.5-turbo/blob/main/Screenshots/Upload%20file%201.PNG?raw=true)
![App Screenshot](https://github.com/bileldhambri/PDF-text-embeddings-chatgpt3.5-turbo/blob/main/Screenshots/Upload%20file%202.PNG?raw=true)
![App Screenshot](https://github.com/bileldhambri/PDF-text-embeddings-chatgpt3.5-turbo/blob/main/Screenshots/Question%201.PNG?raw=true)
![App Screenshot](https://github.com/bileldhambri/PDF-text-embeddings-chatgpt3.5-turbo/blob/main/Screenshots/answer.PNG?raw=true)
