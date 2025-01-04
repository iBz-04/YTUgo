import requests
import folium

# API key & endpoint
api_key = 'API'
endpoint = 'https://api.openrouteservice.org/v2/directions/driving-car'

# Define the coordinates
coordinates = [[28.898495, 41.020884], [28.889969, 41.028267]]

# Set up the parameters
params = {
    'api_key': api_key,
    'start': f"{coordinates[0][0]},{coordinates[0][1]}",
    'end': f"{coordinates[1][0]},{coordinates[1][1]}"
}

# Making request
response = requests.get(endpoint, params=params)
data = response.json()



# Extracting the route 😃
route = data['features'][0]['geometry']['coordinates']

# Convert route to [lat, lon] format for folium
route_latlon = [(coord[1], coord[0]) for coord in route]

# Create a map centered around the starting point
m = folium.Map(location=route_latlon[0], zoom_start=15)

# start and end points
folium.Marker(route_latlon[0], tooltip='Main Entrance (Gate A)', icon=folium.Icon(color='green')).add_to(m)
folium.Marker(route_latlon[-1], tooltip='Faculty of Electrical and Electronics', icon=folium.Icon(color='red')).add_to(m)

# Drawing the route
folium.PolyLine(route_latlon, color='blue', weight=5, opacity=0.7).add_to(m)

m.save('ytu_davutpasa_route.html')