from models import chatGptTurbo, marellaGpt

class Models():

    currentModel = ""

    models = {
        "ChatGPT-3.5 Turbo" : chatGptTurbo.ChatGptTurbo(),
        "marella/gpt-2-ggml" : marellaGpt.MarellaGpt()
    }
    
    def setCurrentModel(self, modelName):
        self.currentModel = modelName

    def getCaption(self):
        return self.models[self.currentModel].getCaption()

    def setApiKey(self, apikey):
        self.models[self.currentModel].setApiKey(apikey)

    def getProjectRequest(self, projectName, projectDescription, extraInformation):
        return self.models[self.currentModel].getProjectRequest(projectName, projectDescription, extraInformation)