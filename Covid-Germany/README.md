# Covid Germany

7 day incidence for german counties.

## Data sources

Map and inhabitants count is from: https://opendata-esri-de.opendata.arcgis.com/datasets/esri-de-content::kreisgrenzen-2016-mit-einwohnerzahl

Case count is from: https://github.com/jgehrcke/covid-19-germany-gae/blob/master/cases-rl-crowdsource-by-ags.csv

You might want to update the files in the `/data` folder with current one's.

## How to run

1. Adapt the `plot_counties.py` according to your needs, make sure that the file paths are set correctyl. Depending on your environment you might want to use absolute paths.

2. Install all requirements

3. Run the `plot_counties.py` file, it will generate png plots and a GIF

4. Adapt the `make_video.py`

5. Run the `make_video.py`, it will generate a mp4 file

## Requirments

Take a look in the `requirements.txt`

## Attribution

**Thanks for the data from:**

Risklayer GmbH (www.risklayer.com) and Center for Disaster Management and Risk Reduction Technology (CEDIM) at Karlsruhe Institute of Technology (KIT) and the Risklayer-CEDIM-Tagesspiegel SARS-CoV-2 Crowdsourcing Contributors

**Thanks for the Geodata from:**

Esri Deutschland
