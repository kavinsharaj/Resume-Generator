import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# from langchain.chains import TextGenerationChain

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text):

    ### LLama2 model
    llm=CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':1000,
                              'temperature':0.01})
 
    ## Prompt Template

    template="""
        {input_text}
            """
    
    prompt=PromptTemplate(input_variables=["input_text"],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(input_text=input_text))
    print(response)
    return response






st.set_page_config(page_title="Generate Resume",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Resume 🤖")

input_text=st.text_input("Enter the Resume Topic")

    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text))