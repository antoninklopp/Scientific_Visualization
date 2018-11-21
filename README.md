# Processus de création du fichier paraview

- Import le point nc
- Utiliser le filtre calculator iHat*UGRD + jHat*VGRD
- Utiliser le filtre Glyph et mettre le scale à 0.3
- Utiliser le filtre contour (ne rien changer)
- Utiliser stream tracer "Point Source" en "High resolution source"
  Changer aussi dans representation : "surface" en "surface with edges"

# Lancer le script

```console
me@machine:~$ ./main.sh argument
```
