import streamlit as st
from helpers import texts
from models import modelManager

def main():

    
    modelController = modelManager.Models()

    st.title("Project Brief Creator")
    st.markdown(texts.SubtitleNotes().getText())
    st.divider()

    models = st.selectbox(
        "Model",
        ("ChatGPT-3.5 Turbo", "marella/gpt-2-ggml"),
        index=0,
        placeholder="model"
    )

    if(models == "ChatGPT-3.5 Turbo"):
        modelController.setCurrentModel(models)
        apikey = st.text_input("Open Api Key")
        st.caption(modelController.getCaption())
        modelController.setApiKey(apikey)

    if(models == "marella/gpt-2-ggml"):
        modelController.setCurrentModel(models)
        st.caption(modelController.getCaption())

    st.divider()
    projectName = st.text_input("Project Name")
    projectDescription = st.text_area("Project Description")
    extraInformation = st.text_area("Extra Information")

    generateButton = st.button("Generate")
    if(generateButton):
        with st.spinner("Loading..."):
           projectRequest = modelController.getProjectRequest(projectName, projectDescription, extraInformation)
           result = st.text_area("Project Brief", value=projectRequest)



    


    

if __name__ == '__main__':
    main()