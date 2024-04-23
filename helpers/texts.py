class Text():
    text = ""

    def getText(self):
        return self.text
    
class SubtitleNotes(Text):
    text = """
    This app will help you create a project brief with the help of AI. 
    1. First, choose a model. _Note: You will need an api key to use most models. You may also choose an open-source model but the results may not be very good._ 
    2. After choosing a model, input a project name, description, and any extra information. 
    3. Finally, press **"Generate"** to have AI create your project brief.
    """