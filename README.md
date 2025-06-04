# programmieruebung_2-5
Aufgaben 2-5 für Progrommieren 2
Herzfrequenz- und Leistungsanalyse mit Streamlit 

Diese Streamlit-App ermöglicht es, Trainingsdaten zu analysieren und visuell darzustellen. Im Fokus stehen dabei die Herzfrequenz in Bezug auf individuell definierte Trainingszonen sowie die erbrachte Leistung. Die App bietet eine übersichtliche Visualisierung in einem Plot mit eingefärbten Herzfrequenzzonen und gibt zusätzlich statistische Kennwerte wie durchschnittliche Leistung pro Zone aus.

Funktionsumfang:
- Einlesen von Aktivitätsdaten aus einer .csv-Datei
- Berechnung und farbliche Darstellung der Herzfrequenzzonen
- Visualisierung von Herzfrequenz (bpm) und Leistung (Watt)
- Berechnung der durchschnittlichen Leistung pro Zone
- Ausgabe der Verweildauer in den einzelnen Zonen (in Minuten)

Voraussetzungen:
Zum Ausführen des Projekts werden Python und das Paketverwaltungstool PDM benötigt. Falls PDM noch nicht installiert ist, kann es über pip installiert werden:
pip install pdm 

Projekt ausführen:
1. Projektordner klonen oder herunterladen 
2. Im Projektverzeichnis folgende Befehle ausführen:
pdm init 
pdm add streamlit plotly pandas numpy 

Die App starten mit:
streamlit run main.py

Datenstruktur:
Die Datei activity.csv im Ordner data/activities enthält die Herzfrequenz- und Leistungsdaten. Diese werden in read_pandas.py eingelesen und verarbeitet.

Screenshot der App:

![Screenshot der App1](programmieruebung_2-5/Screenshot App1.png)
![Screenshot der App2](programmieruebung_2-5/Screenshot App2.png)
![Screenshot der App3](programmieruebung_2-5/Screenshot App3.png)

