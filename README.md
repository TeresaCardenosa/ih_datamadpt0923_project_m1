
# Madrid en bici 🚲

Find your nearest BiciMad or BiciPark to your location. 📌

Specify whether you need to pick up (BiciMad) or drop off (BiciPark) a bike, and the garden or park in Madrid where you are as the point of origin.

🔜 This way, you will find out which is the closest station and the distance of the journey.


## Installation

For the proper functioning of the project, you will need:

```bash
  Python version 3.10.13
```
Additionally, you must install the following libraries:

```bash
import argparse
import pandas as pd
from fuzzywuzzy import process
from shapely.geometry import Point
import geopandas as gpd
```

## Data 📚

The project works with 2 main datasources:

- Parks and gardens of Madrid -> you can obtain this .JSON through the [Portal de Datos Abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/).
- CSV Files. The files named *bicimad_stations* and *bicipark_stations* contain the necessary information for BiciMad/BiciPark stations.


Also, in the **Data** folder, you will find two already created versions of CSV.

- *interes_bicimad* y *interes_bicipark* are the final results of applying the modules to obtain the dataframes that the project works with.

## Folder structure

└── project
    ├── __trash__
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   └── dev_notebook_.ipynb
    ├── package1
    │   ├── bicimad.py
    │   ├── bicipark.py
    │   ├── concat_parques_bicis.py
    │   ├── geo_calculations.py
    │   └── parques_jardines.py
    └── data
        ├── bicimad_stations.csv
        ├── bicipark_stations.csv
        └── results (interes_bicimad/interes_bicipark)

## Demo

The project, available to run from the main.py file, works with three Argparse arguments:

1⃣ -r --> Choose between Bicimad or Bicipark.
As a result of executing this argument, you will get the complete dataframe of parks and gardens with their corresponding nearest stations.

2⃣ -c --> Choose between Bicimad or Bicipark

3⃣ -u --> Determine your location as the point of origin (in this case, which park or garden in Madrid you are in).

When you execute these last two arguments, the project will return the nearest Bicimad/Bicipark station to the location, based on the category and location you have entered.

![gif_codigo_main](https://github.com/TeresaCardenosa/ih_datamadpt0923_project_m1/assets/140433014/e9d399c6-9d3b-4b6c-88bd-751f47f0dfd7)


## Optimizations 💻

Do you want to improve the code?
Can you think of how to implement it?
Would you like to connect it to the BiciMad API to see real-time bike availability?
Or perhaps generate a map on Google that guides you on the way?

Go ahead! 

![force](https://github.com/TeresaCardenosa/ih_datamadpt0923_project_m1/blob/main/images/force.jpg)

## Status 👀

This is the module 1 project for the Data Analytics bootcamp at Ironhack.


## Feedback

📲 If you have any feedback, feel free to contact me through [LinkedIn](https://www.linkedin.com/in/mteresacardenosadeheras/).


## Author

- [@teresacardenosa](https://www.github.com/TeresaCardenosa)






 


 

