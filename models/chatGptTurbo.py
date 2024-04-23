from openai import OpenAI
from helpers import prompts
from models import baseModel

class ChatGptTurbo(baseModel.model):
    name = "ChatGPT-3.5 Turbo"
    caption = "_To use this app, you will need to have an OpenAI API Key. Access it from this link: https://platform.openai.com/account/api-keys_"

    def getProjectRequest(self, projectName, projectDescription, extraInformation):
        projectInformation = f"Project Name: {projectName}, Project Description: {projectDescription}, Extra Information: {extraInformation}"
        basePrompt = prompts.BasePrompt()
        prompt = [
                    {
                    "role": "system",
                    "content": basePrompt.getSystemPrompt()
                    },
                    {   
                    "role": "user",
                    "content": basePrompt.getUserPrompt()
                    },
                    {
                    "role": "assistant",
                    "content": basePrompt.getAssistantPrompt()
                    }, 
                    {
                    "role": "user",
                    "content": projectInformation
                    }
                ]
        
        return getChatGptTurboResponse(self.apikey, prompt)

def getChatGptTurboResponse(apikey, prompt): 
    openai_client = OpenAI(api_key=apikey)

    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
        
    except Exception as e:
        return f"An error occured: {str(e)}"