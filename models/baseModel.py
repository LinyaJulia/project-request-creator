class model():
    name = None
    caption = None
    apikey = None
    requiresApiKey = False

    def getCaption(self):
        return self.caption

    def setApiKey(self, apiKey):
        self.apikey = apiKey
    
    def checkApiKey(self):
        if(self.apikey):
            return True
        else:
            return False

    def checkIfApiRequirementFulfilled(self):
        if(self.requiresApiKey):
            if(self.apikey):
                return True
            else: 
                return False
        else: 
            return True

    def getProjectRequest(self, projectName, projectDescription, extraInformation):
        return None