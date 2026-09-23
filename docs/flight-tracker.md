# Global flight tracker

The flight page is a standalone tracker-style dashboard with a rotating, draggable globe, simplified world outlines, aircraft markers, headings, filters, a searchable aircraft list, demo traffic, JSON import, and optional live polling.

## Live data

The default example endpoint is the OpenSky Network states endpoint. Availability from a local HTML file depends on the provider's current API policy, authentication requirements, and browser CORS behavior.

You can paste another permitted JSON endpoint into the Live data endpoint field. The parser accepts:
- OpenSky `states` arrays
- `aircraft` arrays
- `data` arrays
- Generic arrays with common latitude/longitude/callsign/altitude fields

This project does not scrape Flightradar24, bypass access controls, or access aircraft systems.

## Demo mode

Click **Demo traffic** for 75 synthetic aircraft. Demo coordinates and callsigns are not real flights.
