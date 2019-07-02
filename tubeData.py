import csv
import requests

response = requests.get('https://api.tfl.gov.uk/Line/Mode/tube?app_id=APPID&app_key=APPKEY')

line_data = response.json() if response and response.status_code == 200 else None

for line in line_data:
    lineId = line['id']
    response = requests.get('https://api.tfl.gov.uk/Line/{}/StopPoints?app_id=APPID&app_key=APPKEY'.format(lineId))

    stop_data = response.json() if response and response.status_code == 200 else None

    with open('{}.csv'.format(lineId), 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Station', 'Latitude', 'Longitude'])
        for stops in stop_data:
            Name = stops['commonName']
            Longitude = stops['lon']
            Latitude = stops['lat']

            writer.writerow([Name, Latitude, Longitude])