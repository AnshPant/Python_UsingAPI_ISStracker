#using international space station API
import requests

#request module is the best module to work with api like errors and status no need to check if again and again for different status code
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude =  data["iss_position"]["longitude"]
latitude =  data["iss_position"]["latitude"]
iss_position = (longitude,latitude)
print(iss_position)

