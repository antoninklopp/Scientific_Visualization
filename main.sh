#!/bin/sh

#Enlever tous les anciens fichiers image
rm images/*.png > /dev/null

# Parametre 1 : Type de format (ex : SP1)
for i in {1..7}
do
    rm *.grib2 > /dev/null

    # Enlever les anciens output files
    rm *.nc > /dev/null

    echo $((($i-1)*6 - 5))
    python3 RequeteArome.py $((($i-1)*6 - 5)) $1 # intervalle de 6 heures entre chaque données.

    NOM_FICHIER="$(ls *.grib2 | head -n1)"

    if [ -z "$NOM_FICHIER" ]
    then
      echo "Le fichier semble ne pas avoir été téléchargé"
      exit
    fi

    # Convertir fichier en grib2
    ./wgrib2 $NOM_FICHIER -netcdf output.nc > /dev/null

    # Process avec paraview
    pvpython process_data.py output.nc $i > /dev/null

done

python3 animatekml.py

# Ouverture dans google earth
google-earth TimeSpan.kml
