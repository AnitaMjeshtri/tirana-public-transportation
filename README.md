#  Tirana Public Transportation Data
This repository contains public transportation data of Tirana sourced from OpenStreetMap. The provided Python script utilizes the Overpy library with Overpass API queries to convert XML data into detailed JSON format.

## Usage
**Clone the Repository:**
   ```bash
   git clone git@github.com:AnitaMjeshtri/Tirana_PublicTransportation.git
or
   git clone https://github.com/AnitaMjeshtri/Tirana_PublicTransportation.git
```
## Script Details
The Python script in this repository performs the following steps:

- Parses OSM XML data using the `xml.etree.ElementTree` module.
- Utilizes the `Overpy` library to query the `Overpass API` for additional node details.
- Converts the obtained data into a structured JSON format, excluding 'stop_position' tags.
- Writes the resulting JSON data to the specified output file.

