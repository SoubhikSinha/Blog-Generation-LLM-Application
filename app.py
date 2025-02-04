# Importing the necessary libraries
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from Llama-2 model
def getLlamaResponse(input_text, no_words, blog_style):
    # Calling the Llama-2 model
    llm = CTransformers(model = 'models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens' : 256,
                                  'temperature' : 0.01})
    
    # Promt template
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
        """
    
    prompt = PromptTemplate(input_variables = ["blog_style", "input_text", "no_words"],
                            template = template)
    
    # Generating the response from the Llama-2 model
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words = no_words))
    print(response)
    return response


# Streamlit application
st.set_page_config(page_title = "Generate Blogs",
                   page_icon = "🤖",
                   layout = "centered",
                   initial_sidebar_state = "collapsed")

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic : ") # Input Box

# Creating columns for additionl fields
col1, col2 = st.columns([5, 5]) # Width of the columns

with col1: # Column #1 will contain the number of words in that blog
    no_words = st.text_input('No. of Words')

with col2: # Column #2 will contain drop-down menu for the below
    blog_style = st.selectbox('Writing the blog for : ', 
                              ('Researchers', 'Data Scientists', 'Common People'), index = 0)

submit = st.button("Generate") # Generate Button


# Final response
if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))

