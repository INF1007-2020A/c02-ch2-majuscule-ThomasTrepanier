#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    increment = 32
    LIMIT_MAJ = 90
    for lettre in mot:
        # TODO completer la fonction ici
        letterCode = ord(lettre)

        if letterCode > 90:
            letterCode -= increment
        else:
            letterCode += increment

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
