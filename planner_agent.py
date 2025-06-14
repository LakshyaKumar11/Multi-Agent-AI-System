from agents.launch_info_agent import LaunchInfoAgent
from agents.weather_check_agent import WeatherCheckAgent
from agents.delay_analyzer_agent import DelayAnalyzerAgent

class PlannerAgent:
    def execute(self, goal):
        if "launch" in goal:
            launch_info = LaunchInfoAgent().get_launch_info()
            weather_info = WeatherCheckAgent().get_weather(launch_info)
            analysis = DelayAnalyzerAgent().analyze(launch_info, weather_info)
            return analysis
        else:
            return {"error": "Unsupported goal"}
