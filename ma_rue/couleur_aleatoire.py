from ma_rue import rue, affiche
from random import randint

def couleur_aleatoire():

    couleur=f"rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})"


    return couleur

# Tests
if __name__=='__main__':
    affiche(rue)
    couleur = couleur_aleatoire()
    rue.fill_style = couleur
    rue.fill_rect(0, 0, rue.width, rue.height)
    rue.font = '48px Lucida Console'
    rue.text_align = 'center'
    rue.stroke_text(couleur, rue.width/2, rue.height/2)

    
    # Autres test
    from time import sleep
    affiche(rue)
    for i in range(30) :
        couleur = couleur_aleatoire()
        rue.fill_style = couleur
        rue.fill_rect(0, 0, rue.width, rue.height)
        rue.font = '48px Lucida Console'
        rue.text_align = 'center'
        rue.stroke_text(couleur, rue.width/2, rue.height/2)
        sleep(1)