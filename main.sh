#!/bin/sh

print_help() {
    echo "Visualisation scientifique

Lancer ./main.sh

--default (ou sans argument) : visualisation de la
carte avec iso valurs, lignes de courant et temperature

--iso : visualisation des lignes iso valeurs de temperature

--temp : visualisation de la température seule

--max_intervalles=n : Si on ne veut que n intervalles de temps (default : max : 7)

--package=package : Changer le package (default sp1)
"
}

#Enlever tous les anciens fichiers image
mkdir images > /dev/null 2>&1
rm images/*.png > /dev/null 2>&1

TYPE_COURBE="--default"
TYPE_PACKAGE="IP1"
MAX_INTERVALLES=7

for i in "$@"
do
case $i in
    -h|--help)
    print_help
    exit
    ;;
    --max_intervalles=*|-m=*)
        MAX_INTERVALLES="${i#*=}"
        shift
    ;;
    --package=*|-p=*)
        TYPE_PACKAGE="${i#*=}"
        shift
    ;;
    --iso)
        TYPE_COURBE="--iso"
        echo "Carte des iso valeurs"
        shift
    ;;
    --temp)
        TYPE_COURBE="--temp"
        echo "Carte des temperatures"
        shift
    ;;
    *)
          # unknown option
    ;;
esac
done

# Parametre 1 : Type de format (ex : SP1)
for (( i=1; i<=$MAX_INTERVALLES; i++ ))
do
    rm *.grib2 > /dev/null 2>&1

    # Enlever les anciens output files
    rm *.nc > /dev/null 2>&1

    echo "Téléchargement carte $i"
    python3 RequeteArome.py $((($i-1)*6 - 5)) $TYPE_PACKAGE # intervalle de 6 heures entre chaque données.

    NOM_FICHIER="$(ls *.grib2 | head -n1)" > /dev/null 2>&1

    while [ -z "$NOM_FICHIER" ]
    do

      echo "Le fichier semble ne pas avoir été téléchargé, nous reessayons dans 30 secondes. "

      sleep 30

      rm *.grib2 > /dev/null 2>&1

      # Enlever les anciens output files
      rm *.nc > /dev/null 2>&1

      python3 RequeteArome.py $((($i-1)*6 - 5)) $1 > /dev/null 2>&1 # intervalle de 6 heures entre chaque données.

      NOM_FICHIER="$(ls *.grib2 | head -n1)" > /dev/null 2>&1

  done

    # Convertir fichier en grib2
    ./wgrib2 $NOM_FICHIER -netcdf output.nc > /dev/null 2>&1

    # Process avec paraview
    case $TYPE_COURBE in
        --iso)
        pvpython process_data_iso.py output.nc $i > /dev/null 2>&1
        ;;
        --temp)
        pvpython process_data_temp.py output.nc $i > /dev/null 2>&1
        ;;
        --default)
        pvpython process_data.py output.nc $i > /dev/null 2>&1
        ;;
    esac


done

# Création du fichier KML
python3 animatekml.py

# On ne peut pas charger de fichier depuis la ligne de commande.
# On propose donc à l'utilisateur d'ouvrir le fichier à la main.
echo "Vous pouvez maintenant ouvrir le fichier meteo.kml"
