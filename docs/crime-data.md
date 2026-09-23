# Crime data

The crime dashboard uses incident records supplied from public or official sources.

## JSON

Simple array:
```json
[
  {"id":"123","date":"2026-01-15","category":"Burglary","location":"Example","lat":20.29,"lon":85.82}
]
```

It also accepts a GeoJSON FeatureCollection, using feature properties and point coordinates.

## CSV

Use a header row. Common fields are:
`id,date,category,location,lat,lon`

## Privacy

Use public incident information and avoid unnecessary identifiers such as names, phone numbers, private addresses, license plates, or other data that can identify individuals.

Live crime feeds vary by jurisdiction and may require API keys or have specific publication/usage rules. This project therefore does not hard-code an unverified live endpoint.
