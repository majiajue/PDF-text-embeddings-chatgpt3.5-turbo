import streamlit as st
import pytesseract
import openai
from pytesseract import Output, TesseractError
from functions import convert_pdf_to_txt_file, displayPDF
from openai.embeddings_utils import get_embedding
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from streamlit_chat import message 

openai.api_key ="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"
# embedding model parameters
#embedding_model = "text-embedding-ada-002"
#embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
#max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

def answer_question(message_log):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,   # The conversation history up to this point, as a list of dictionaries      
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
    )
    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content





st.set_page_config(page_title="PDF Text Embeddings")

pdf_file = st.file_uploader("Load your PDF", type="pdf")
hide="""
<style>
footer{
	visibility: hidden;
    	position: relative;
}
.viewerBadge_container__1QSob{
  	visibility: hidden;
}
#MainMenu{
	visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)
if pdf_file:
    path = pdf_file.read()
    # display document
    with st.expander("Display document"):
        displayPDF(path)
    text_data_f, nbPages,df = convert_pdf_to_txt_file(pdf_file)
    totalPages = "Pages: "+str(nbPages)+" in total"
    st.info(totalPages)
    st.write(df)
    #st.write(text_data_f)
    st.download_button("Download txt file", text_data_f)
    df['ada_embedding']= df.text.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
    st.write(df)
if 'generated' not in st.session_state:
    st.session_state['generated']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]
def get_text():
    input_text=st.text_input("Question :",key="input")
    return input_text
with st.form('form',clear_on_submit=True):
    user_input=get_text()
    submitted=st.form_submit_button('ASK')
if submitted :
    #st.write(get_embedding(user_input, model='text-embedding-ada-002'))
    question_embedding=get_embedding(user_input, model='text-embedding-ada-002')
    question_array = np.array(question_embedding)
    liste_similarite=[]
    for i in df["ada_embedding"]:
        array_answer=np.array(i)
        # calculer la similarité cosinus entre l'embedding de la question et tous les embeddings dans la dataframe
        similarites = cosine_similarity(question_array.reshape(1,-1), array_answer.reshape(1,-1))
        #st.write(similarites[0][0])
        liste_similarite.append(similarites[0][0])
    df['similarite'] = liste_similarite
    # trier les textes en fonction de leur similarité avec la question
    df = df.sort_values(by="similarite", ascending=False)
    most_similar_text = df.iloc[0]["text"]
    st.write(df)
    message_log = [
        {"role": "system", "content": most_similar_text}
    ]
    message_log.append({"role": "user", "content": user_input})
    #st.write(most_similar_text)
    answer = answer_question(message_log)
    #st.write(answer)
     #store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer)
if st.session_state['generated']:
        for i  in range(len(st.session_state['generated'])-1,-1,-1):
            message(st.session_state['generated'][i],key=str(i))
            message(st.session_state['past'][i],is_user=True,key=str(i)+'_User')


