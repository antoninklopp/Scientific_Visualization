#!/bin/sh

rm *.grib2 > /dev/null

# Parametre 1 : heure
# Parametre 2 : Type de format
python3 RequeteArome.py $1 $2

# Enlever les anciens output files
rm output.nc > /dev/null

NOM_FICHIER="$(ls *.grib2 | head -n1)"

if [ -z "$NOM_FICHIER" ]
then
  echo "Le fichier semble ne pas avoir été téléchargé"
  exit
fi

# Convertir fichier en grib2
wgrib2 $NOM_FICHIER -netcdf output.nc

# Process avec paraview
pvpython process_data.py output.nc

# Ouverture dans google earth
