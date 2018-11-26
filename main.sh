#!/bin/sh

#Enlever tous les anciens fichiers image
rm images/*.png > /dev/null 2>&1

for i in "$@"
do
case $i in
    -h|--help)
    echo "Visualisation scientifique

Lancer ./main.sh argument

--default (ou sans argument) : visualisation de la
carte avec iso valurs, lignes de courant et temperature

--iso : visualisation des lignes iso valeurs de temperature

--temp : visualisation de la température seule"
    exit
    shift # past argument=value
    ;;
    *)
          # unknown option
    ;;
esac
done

# Parametre 1 : Type de format (ex : SP1)
for i in {1..7}
do
    rm *.grib2 > /dev/null 2>&1

    # Enlever les anciens output files
    rm *.nc > /dev/null 2>&1

    echo "Téléchargement carte $i"
    python3 RequeteArome.py $((($i-1)*6 - 5)) $1 > /dev/null 2>&1 # intervalle de 6 heures entre chaque données.

    NOM_FICHIER="$(ls *.grib2 | head -n1)" > /dev/null 2>&1

    while [ -z "$NOM_FICHIER" ]
    do

      echo "Le fichier semble ne pas avoir été téléchargé, nous reessayons dans 30 secondes. "

      sleep 30

      rm *.grib2 > /dev/null 2>&1

      # Enlever les anciens output files
      rm *.nc > /dev/null 2>&1

      echo $((($i-1)*6 - 5))
      python3 RequeteArome.py $((($i-1)*6 - 5)) $1 > /dev/null 2>&1 # intervalle de 6 heures entre chaque données.

      NOM_FICHIER="$(ls *.grib2 | head -n1)"

  done

    # Convertir fichier en grib2
    ./wgrib2 $NOM_FICHIER -netcdf output.nc > /dev/null 2>&1

    # Process avec paraview
    for i in "$@"
    do
    case $i in
        --iso)
        pvpython process_data_iso.py output.nc $i > /dev/null 2>&1
        shift
        ;;
        --temp)
        pvpython process_data_temp.py output.nc $i > /dev/null 2>&1
        shift
        ;;
        *)
        pvpython process_data.py output.nc $i > /dev/null 2>&1
        ;;
    esac
    done


done

python3 animatekml.py

# Ouverture dans google earth
google-earth TimeSpan.kml
