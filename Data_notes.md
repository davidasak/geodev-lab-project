# Data notes

## Boundary
- Source: https:
- Extracted: [9/12/2026]
- 1 feature, polygon

## OSM roads, extracted via QuickOSM
- Query: highway=+ within boundary
- Extracted: [9/12/2026]
- 994 features, lines

## OSM residential areas, extracted via QuickOSM
- Query: landuse within boundary
- Extracted: [9/12/2026]
- 1 feature, polygon

## Hospital, extracted via Google Earth Pro
- Extracted: [9/12/2026]
- 9 feature, polygon

## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Shomolu, extracted from GRID3 wards
- All layers clipped to study area, then reprojected to EPSG:32631 (UTM 31N)
- Area check: Shomolu 10.296550216138387 km2, matches published figure (Size: Approximately 14.6 km² (some estimates cite about 10.3 km² for the core municipal zone).
- Working files in data/processed/, raw files untouched
