#! /usr/bin/env python3
# coding:utf-8

import json


def ouverture_fichier():

    with open("P01_02_planning.json") as fichier:
        lecture_fichier = json.load(fichier)

        affichage_planning = [projet["projet"] for projet in lecture_fichier]

    return affichage_planning


def affichage_planning(param):

    print(f"\n=============================================================================\n\
{'Projet'.center(10)}|{'Temps/jours'.center(15)}|{'Date'.center(30)}|{'Soutenance'.center(20)}")

    for planning in param:
        print(f"-----------------------------------------------------------------------------\n\
{str(planning[0]).center(10)}|{str(planning[4]['Temps alloué']).center(15)}|\
{str(planning[5]['Date']).center(30)}|{str(planning[6]['Soutenance']).center(20)}")
    print("=============================================================================\n")


affichage_planning(ouverture_fichier())
