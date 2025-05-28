# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd
import numpy as np

import plotly.io as pio 
pio.renderers.default = "browser"
# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/activities/activity.csv")
                   

    time = np.arange(0, len(df))
    df["Time"] = time
    # Setzt die Columnnames im Dataframe
    #df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df


# %%

def make_plot(df):
    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df, x="Time", y=["PowerOriginal", "HeartRate"])
    return fig

    df = pd.DataFrame(data)

  
if __name__ == "__main__":
    #Lese die Datei ein
    df = read_my_csv()
    print(df.head())

    #Erstelle einen Plot
    fig = make_plot(df)

    #Zeige den Plot an 
    fig.show()
