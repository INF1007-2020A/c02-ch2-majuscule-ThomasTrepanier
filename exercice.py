#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    dist_entre_min_et_maj = ord('a') - ord('A')
    code_min_des_maj = ord('A')
    code_max_des_maj = ord('Z')
    code_min_des_min = ord('a')
    code_max_des_min = ord('z')
    for lettre in mot:
        # TODO completer la fonction ici
        letterCode = ord(lettre)

        if letterCode <= code_max_des_maj and letterCode >= code_min_des_maj:
            letterCode += dist_entre_min_et_maj
        elif letterCode <= code_max_des_min and letterCode >= code_min_des_min:
            letterCode -= dist_entre_min_et_maj
#lol
        lettre = chr(letterCode)
        resultat += lettre
    return resultat
#test

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
