from langchain_community.llms import CTransformers
from helpers import prompts
from models import baseModel


class MarellaGpt(baseModel.model):
    name = "marella/gpt-2-ggml"
    caption = "_Disclaimer: This model does not give very good results for this use case. It has been left here for testing and comparison purposes._"
    requiresApiKey = False

    def getProjectRequest(self, projectName, projectDescription, extraInformation):
        basePrompt = prompts.BasePrompt()
        projectInformation = f"Project Name: {projectName}, Project Description: {projectDescription}, Extra Information: {extraInformation}"
        prompt = f"System: {basePrompt.getSystemPrompt()}, User: {basePrompt.getUserPrompt()}, Assistant: {basePrompt.getAssistantPrompt()}, User: {projectInformation}"
        return getMarellaGptResponse(prompt)
        
    
def getMarellaGptResponse(prompt):
    try:
        llm = CTransformers(model="marella/gpt-2-ggml")
        return(llm("prompt"))
    
    except Exception as e:
        return f"An error occured: {str(e)}" 