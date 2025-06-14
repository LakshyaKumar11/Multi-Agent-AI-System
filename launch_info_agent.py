import requests

class LaunchInfoAgent:
    def get_launch_info(self):
        res = requests.get("https://api.spacexdata.com/v4/launches/next")
        data = res.json()
        return {
            "name": data.get("name"),
            "date_utc": data.get("date_utc"),
            "launchpad": data.get("launchpad")
        }
