#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    dist_entre_min_et_maj = ord('a') - ord('A')
    LIMIT_MAJ = ord('z')
    for lettre in mot:
        # TODO completer la fonction ici
        letterCode = ord(lettre)

        if letterCode > LIMIT_MAJ:
            letterCode -= dist_entre_min_et_maj
        else:
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
