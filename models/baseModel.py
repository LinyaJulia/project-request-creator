class model():
    name = None
    caption = None
    apikey = None

    def getCaption(self):
        return self.caption

    def setApiKey(self, apiKey):
        self.apikey = apiKey

    def getProjectRequest(self, projectName, projectDescription, extraInformation):
        return None