#!/bin/sh

# rm *.grib2 > /dev/null

# Parametre 1 : heure (ex : 0)
# Parametre 2 : Type de format (ex : SP1)
# python3 RequeteArome.py $1 $2

# Enlever les anciens output files
# rm output.nc > /dev/null

NOM_FICHIER="$(ls *.grib2 | head -n1)"

if [ -z "$NOM_FICHIER" ]
then
  echo "Le fichier semble ne pas avoir été téléchargé"
  exit
fi

# Convertir fichier en grib2
./wgrib2 $NOM_FICHIER -netcdf output.nc

# Process avec paraview
pvpython process_data.py output.nc




# Ouverture dans google earth
# google-earth .kml
