import streamlit as st
from helpers import texts, exporter
from models import modelManager

def main():
    st.session_state.modelController = modelManager.Models()
    if "projectRequest" not in st.session_state:
        st.session_state.projectRequest = ""

    st.title("Project Brief Creator")
    st.markdown(texts.SubtitleNotes().getText())

    with st.expander("Set model"):
        models = st.selectbox(
            "Model",
            ("ChatGPT-3.5 Turbo", "marella/gpt-2-ggml"),
            index=0,
            placeholder="model"
        )

        if(models == "ChatGPT-3.5 Turbo"):
            st.session_state.modelController.setCurrentModel(models)
            apikey = st.text_input("Open Api Key")
            st.caption(st.session_state.modelController.getCaption())
            st.session_state.modelController.setApiKey(apikey)

        if(models == "marella/gpt-2-ggml"):
            st.session_state.modelController.setCurrentModel(models)
            st.caption(st.session_state.modelController.getCaption())

    with st.expander("Set project inputs"):
        projectName = st.text_input("Project Name")
        projectDescription = st.text_area("Project Description")
        extraInformation = st.text_area("Extra Information")

    generateButton = st.button("Generate", use_container_width=True, disabled=not st.session_state.modelController.checkIfApiKeyRequirementFulfilled())
    result = st.empty()
    result.text_area("**Project Brief**", height=300)

    if(generateButton):
        with st.spinner("Loading..."):
           st.session_state.projectRequest = st.session_state.modelController.getProjectRequest(projectName, projectDescription, extraInformation)
           result.text_area("**Project Brief**", value=st.session_state.projectRequest, height=300)
           exportBtn = st.download_button("Export", data=st.session_state.projectRequest, file_name="project_brief.txt")


if __name__ == '__main__':
    main()