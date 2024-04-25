from models import chatGptTurbo, marellaGpt
import streamlit as st

class Models():

    st.session_state.currentModel = ""
    st.session_state.models = ""

    def __init__(self):
        if "currentModel" not in st.session_state:
            st.session_state.currentModel = ""
        if "models" not in st.session_state:
            st.session_state.models = ""

    st.session_state.currentModel = ""

    st.session_state.models = {
        "ChatGPT-3.5 Turbo" : chatGptTurbo.ChatGptTurbo(),
        "marella/gpt-2-ggml" : marellaGpt.MarellaGpt()
    }
    
    def setCurrentModel(self, modelName):
        st.session_state.currentModel = modelName

    def getCaption(self):
        return st.session_state.models[st.session_state.currentModel].getCaption()

    def setApiKey(self, apikey):
        st.session_state.models[st.session_state.currentModel].setApiKey(apikey)

    def getProjectRequest(self, projectName, projectDescription, extraInformation):
        return st.session_state.models[st.session_state.currentModel].getProjectRequest(projectName, projectDescription, extraInformation)
    
    def checkIfApiKeyRequirementFulfilled(self):
        return st.session_state.models[st.session_state.currentModel].checkIfApiRequirementFulfilled()