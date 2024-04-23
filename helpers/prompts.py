class BasePrompt:
    systemPrompt = """
    You are an expert project manager. Based on certain inputs, you need to create a concise project brief that follows this format:
    Project Name, Project Description, Project Scope, Objectives, Stakeholders, Resource Constraints, Timeline, Approach.
    """

    userPrompt = """
    Project Name: Green Horizon
    Project Description: Project invovling improving green spaces for better environment sustainability and well being for the community. The goal is to improve three urban parks.
    Extra Information: This needs to involve observing the current part facilities and we need to set up community engagement programs.
    """

    assistantPrompt = """
    You are an expert project manager. Based on certain inputs, you need to create a concise project brief that follows this format:
    Project Name, Project Description, Project Scope, Objectives, Stakeholders, Resource Constraints, Timeline, Approach.
    Here is an example of a project brief: 

    Project Brief
    Project Name: Green Horizon Initiative

    Project Description:
    The Green Horizon Initiative is a comprehensive project aimed at improving urban green spaces to enhance environmental sustainability and community well-being. The initiative seeks to revitalize three major urban parks, integrating eco-friendly infrastructure and community-focused amenities.

    Project Scope:

    Assessment of current park facilities and infrastructure.
    Design and implementation of sustainable park features such as solar-powered lighting and water-efficient landscapes.
    Community engagement programs to foster local participation and awareness.
    Installation of new recreational facilities tailored to all age groups.
    Objectives:

    Increase the urban green cover by 30 percent in the targeted areas.
    Enhance community access to high-quality recreational spaces.
    Promote environmental awareness and sustainable practices among residents.
    Improve overall air quality and contribute to the city’s climate resilience.
    Stakeholders:

    City Council
    Local Community Groups
    Environmental NGOs
    Urban Planning Department
    Local Businesses
    Resource Constraints:

    Budget capped at $2 million.
    Limited access to specialized green technology providers.
    Dependency on volunteer participation for some community initiatives.
    Timeline:

    Phase 1: Planning and Design (January 2024 - March 2024)
    Stakeholder meetings
    Completion of initial park assessments
    Finalization of park design and features
    Phase 2: Implementation (April 2024 - October 2024)
    Construction and renovation activities
    Installation of new park features and facilities
    Initiation of community engagement programs
    Phase 3: Evaluation and Maintenance (November 2024 - December 2024)
    Assessment of project impact
    Training for ongoing maintenance
    Project handover to city management
    Approach:
    The project will adopt a phased approach, ensuring each stage is completed on time and within budget. Collaborative efforts between stakeholders will be emphasized to integrate diverse insights and expertise. Sustainable methods and materials will be prioritized throughout the project to align with environmental objectives.

    Now, create a project brief based on these values: """

    def getSystemPrompt(self):
        return self.systemPrompt
    
    def getUserPrompt(self):
        return self.userPrompt
    
    def getAssistantPrompt(self):
        return self.assistantPrompt