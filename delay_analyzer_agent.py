class DelayAnalyzerAgent:
    def analyze(self, launch_info, weather_info):
        if "error" in weather_info:
            return {
                "launch": launch_info.get("name", "Unknown"),
                "date": launch_info.get("date_utc", "Unknown"),
                "weather": "Unavailable",
                "delay_likelihood": "Unknown",
                "reason": f"Weather data error: {weather_info.get('error')}"
            }

        delay = "No"
        reason = ""

        if weather_info["weather"].lower() in ["thunderstorm", "rain", "snow"]:
            delay = "Likely"
            reason = "Adverse weather conditions"
        elif weather_info["wind_speed"] > 15:
            delay = "Possible"
            reason = "High wind speed"

        return {
            "launch": launch_info["name"],
            "date": launch_info["date_utc"],
            "weather": weather_info,
            "delay_likelihood": delay,
            "reason": reason or "Normal conditions"
        }
