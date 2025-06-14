# Multi-Agent AI System using Google ADK

## Overview
This project builds a modular multi-agent system that plans and routes data between agents to fulfill user-defined goals using public APIs.

## Setup

1. Create a `.env` file with API keys:
```
OPEN_WEATHER_API_KEY=your_openweather_key
NEWS_API_KEY=your_newsapi_key
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main file:
```bash
python main.py
```

## Agents
- **PlannerAgent**: Breaks down goals and routes tasks.
- **LaunchInfoAgent**: Fetches next launch info from SpaceX.
- **WeatherCheckAgent**: Checks weather at launch location.
- **DelayAnalyzerAgent**: Analyzes delay likelihood.

## Sample Goal
"Find the next SpaceX launch, check weather, and determine if it may be delayed."

## License
MIT
