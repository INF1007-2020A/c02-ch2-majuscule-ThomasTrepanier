#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    dist_entre_min_et_maj = ord('a') - ord('A')
    code_min_des_maj = ord('A')
    code_max_des_maj = ord('Z')
    code_min_des_min = ord('a')
    for lettre in mot:
        # TODO completer la fonction ici
        letterCode = ord(lettre)

        if letterCode <= code_max_des_maj and letterCode >= code_min_des_maj:
            letterCode -= dist_entre_min_et_maj
        elif lettercode:
            letterCode += dist_entre_min_et_maj

        lettre = chr(letterCode)
        resultat += lettre
    return resultat


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
