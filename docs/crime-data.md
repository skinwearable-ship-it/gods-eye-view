# Automatic police/open-data importer

The crime dashboard at `crime/index.html` auto-detects several common public-data layouts.

### JSON formats

**Generic JSON array**

```json
[
  {"id":"123","date":"2026-01-15","category":"Burglary","lat":20.29,"lon":85.82}
]
```

**GeoJSON FeatureCollection**

The importer reads point coordinates and merges the feature `properties`.

**ArcGIS FeatureSet**

The importer reads `features[].attributes` and `features[].geometry`, including common `x/y` geometry.

**Socrata-style JSON**

The importer accepts a top-level `data` array.

### CSV formats

The importer recognizes common aliases used by police/open-data datasets. Examples include:

- `Crime type`, `CrimeType`, `Offense`, `Primary Type`, `OFNS_DESC`
- `Month`, `Date`, `Occurrence Date`, `Reported Date`
- `Latitude` / `Longitude`
- `Location`, `Address`, `Block`, `Location Description`

The CSV parser also handles quoted fields containing commas.

### Privacy

Use public incident records and remove unnecessary personal identifiers before importing. Do not use this tool to track private individuals.

For live feeds, obtain data from the relevant official/open-data publisher and follow its terms of use. The importer is format-focused and does not bypass API keys, access controls, or publication restrictions.
