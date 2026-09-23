# God's Eye View

An open-source **global public-data observatory** plus **authorized local security dashboard**.

## Global layer

The dashboard can load the public USGS earthquake GeoJSON feed for the previous day and plot returned global event coordinates in a lightweight map.

## Authorized local layer

Import JSON reports created by computers you own or are authorized to administer. Reports stay in the browser and are not uploaded by this repository.

## Run

Open `dashboard/index.html`.

- **Refresh global events**: requires Internet access and loads the public earthquake feed.
- **Import authorized endpoint reports**: uses the local collector in `agent/collect.py`.
- **Load demo endpoint**: tests the UI without collecting anything.

## USB

Copy the repository directory to a USB drive. The dashboard is a static HTML file and can run without a local server.

The global layer needs Internet access. The endpoint layer can be used offline.

## Boundaries

This project does not provide covert surveillance, keylogging, credential collection, screen/camera/microphone capture, persistence, or hidden telemetry. Only collect endpoint data where you have authorization.

Treat real endpoint reports as sensitive infrastructure information. Encrypt the USB when appropriate, and do not commit real reports to this public repository.

## Public data source

USGS Earthquake Hazards Program feed:
`https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`
