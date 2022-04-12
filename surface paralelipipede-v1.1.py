# _____       _                                 _           _ _             _       
#/  __ \     | |                               | |         | | |           | |      
#| /  \/_   _| |__   ___  ___     ___ _ __ ___ | |__   __ _| | | __ _ _ __ | |_ ___ 
#| |   | | | | '_ \ / _ \/ __|   / _ \ '_ ` _ \| '_ \ / _` | | |/ _` | '_ \| __/ __|
#| \__/\ |_| | |_) |  __/\__ \  |  __/ | | | | | |_) | (_| | | | (_| | | | | |_\__ \
#\____/\__,_|_.__/ \___||___/    \___|_| |_| |_|_.__/ \__,_|_|_|\__,_|_| |_|\__|___/
#
#Programme de cacul surface parallipipede suivant volume
#Pour faire un round up on fait la division entiere du nombre negatif 
import os
os.chdir("D://Documents/ici") #notez le chemin d'accès où se trouve le le fichier ncubes.txt et où vous voulez que les résultats soit écrit

with open("ncubes.txt", "r") as ini:
    contenu_ini = ini.read()

with open("resultats-v1.1.csv", "w") as resultats:
    nbr_cube = int(contenu_ini)
    volumemin = 0
    i=1
    entete = "Nombre(s) de cubes, Hauteur, Largeur, Longueur, Surface , Cases vides" + "\n"
    resultats.write(entete)
    while i<=nbr_cube :
        a= 1
        b= 1
        c= 1 
        # print("nombre de cubes =>", i)
        volume = 1 
        surface = 1 
        surfacemin = i * 4 + 2 #le parallelipipede le moins bon est le plus long  
        maxa = i ** (1/3.0) #racine cubique 
        maxa = int(-(-maxa//1)) # round up de maxa
        # print("max a =", maxa) 
        while a <= maxa :
            maxb = (i/a) ** (1/2.0) #racine carre
            maxb = int(round(maxb)) #rounddown de maxb 
            # print ("max b =", maxb)
            b = a #initialisation de b on peut commencer la valuer actuelle de a. 
            while  b <= maxb  :
                c = int(-(-i // (a*b)))
                volume = a*b*c
                surface = 2*(a*b+b*c+a*c)
                # print ("a=", a ,"b=",b,"c=", c ,"volume=",volume, "surface=", surface )
                if surface <= surfacemin :
                        
                    amin = a
                    bmin = b
                    cmin = c
                    volumemin = volume
                    surfacemin = surface # on retient toujours la surface minimale
                    # print ("a ,b,c",a,b,c,"surface minimale actuelle = " ,surfacemin)

                b+=1
            a+=1
        casevide = volumemin - i 
        prout = str(i) + "," + str(amin) + "," + str(bmin) + "," + str(cmin) + "," + str(surfacemin) + "," + str(casevide) + "\n"
        resultats.write(prout)
        
        # print ("surface minimale = ", surfacemin , "|", "avec a,b,c" , amin, bmin, cmin, "| ", "max a = ", maxa, "|", "nombre de case vide", casevide, "|", " nombre de cubes", i)
        i+=1
    print("It's the END !")
