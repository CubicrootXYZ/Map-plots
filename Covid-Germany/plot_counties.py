# ALWAYS INCLUDE COPYRIGHT FOR SHAPEFILE:
# Geodaten von esri Deutschland

import matplotlib.pyplot as plt
import geopandas
import pandas
from pylab import text, figtext

# SETTINGS # 
plot = True # set to false for testing without saving files

counties = geopandas.read_file("./data/Kreisgrenzen_2016_mit_Einwohnerzahl.shp")
data = pandas.read_csv("./data/cases_per_countie_risklayer.csv")

# helpers
files = []
cases_last_days = [{}, {}, {}, {}, {}, {}, {}]
tot_cases_last_day = {}

j = 0
for row in data.iterrows(): # iterate over all days
    date_str = row[1]["time_iso8601"].split("T")[0]
    
    inz = []
    i = 0
    
    # move cases by 1 day
    cases_last_days[0] = cases_last_days[1].copy()
    cases_last_days[1] = cases_last_days[2].copy()
    cases_last_days[2] = cases_last_days[3].copy()
    cases_last_days[3] = cases_last_days[4].copy()
    cases_last_days[4] = cases_last_days[5].copy()
    cases_last_days[5] = cases_last_days[6].copy()

    for countie in counties.iterrows(): # iterate over all counties
        ags = countie[1]["AGS"]
        cases = row[1][ags.lstrip("0")]
        inhabitants = counties["EWZ"][i]

        if j == 0:
            cases_last_days[6][ags] = 0
        else:
            cases_last_days[6][ags] = cases - tot_cases_last_day[ags]

        if j >= 7:
            cases_7_days = cases_last_days[6][ags] + cases_last_days[0][ags] + cases_last_days[1][ags] + cases_last_days[2][ags] + cases_last_days[3][ags] + cases_last_days[4][ags] + cases_last_days[5][ags]

            inz.append((cases_7_days/inhabitants)*100000)
            counties["SHAPE_Area"][i] = (cases_7_days/inhabitants)*100000 # not recommend by pandas, but hey it works :)

        tot_cases_last_day[ags] = cases
        i+=1
        
    if j >= 7 and plot:
        counties.plot(legend=True, edgecolor="black", linewidth=0.25, column='SHAPE_Area', cmap="hot_r", vmin=0, vmax=600, missing_kwds={"color": "lightgrey", "edgecolor": "black"})
        figtext(.05,0.05,'Geodaten von esri Deutschland', fontsize=8, ha='left')
        figtext(.05,0.02,'Fallzahlen von github.com/jgehrcke/covid-19-germany-gae', fontsize=8, ha='left')
        plt.axis('off')
        plt.title(f"7 Tage Inzidenz am {date_str}")
        
        filename = f"./plots/{date_str}.png"
        files.append(filename)
        plt.savefig(filename)
        #plt.show() # use this instead of savefig to show the plots
        plt.clf()
        plt.close()

    if j >= 7:
        print(f"Max Inzidenz am {date_str}: {max(inz)}") # plausibilty check
    j+=1

# make GIF from pngs
if plot:
    import imageio
    with imageio.get_writer('./covid_map.gif', mode='I', duration=0.000001) as writer:
        for filename in files:
            image = imageio.imread(filename)
            writer.append_data(image)