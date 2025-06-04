import pandas as pd
import numpy as np
import plotly.io as pio 
import plotly.express as px
import plotly.graph_objects as go
pio.renderers.default = "browser" #nur temporär, damit die Plots im Browser geöffnet werden

def read_my_csv(): 
    df = pd.read_csv("data/activities/activity.csv")
    time = np.arange(0, len(df))
    df["Time"] = time

    #print("Spaltenanzahl:", len(df.columns))
    #print("Spaltennamen:", df.columns.tolist())
    #print(len(df)) 1804

    Leistung = df["PowerOriginal"]
    durschnittliche_Leistung = Leistung.mean()
    #print("Durchschnittliche Leistung:", durschnittliche_Leistung)
    maximale_Leistung = Leistung.max()
    #print("Maximale Leistung:", maximale_Leistung)
    return df 

def add_heart_rate_zones(df, max_hr):
    zones = [] # leere Liste für die Herzfrequenzzonen 
    for hr in df["HeartRate"]:
        prozent = hr / max_hr
        if prozent < 0.6:
            zones.append("Zone 1")
        elif prozent < 0.7:
            zones.append("Zone 2")
        elif prozent < 0.8:
            zones.append("Zone 3")
        elif prozent < 0.9:
            zones.append("Zone 4")
        else:
            zones.append("Zone 5")
    df["HR_Zone"] = zones #damit erstelle ich eine neue Spalte "HR_Zone" im DataFrame, dort steht für jede Herzfrequenz die passende Zone 
    return df

def calculate_heart_rate_zones(df):
    zone_counts = df["HR_Zone"].value_counts().sort_index()
    zone_durations = {zone: count for zone, count in zone_counts.items()} #jetzt in sekunden 
    return zone_durations


def make_plot(df, max_hr):
    fig = go.Figure()

        # Leistungslinie für die rechte Seite (rechte y-Achse)
    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["PowerOriginal"],
        mode='lines',
        name='Leistung (Watt)',
        line=dict(color='blue'),
        yaxis='y2'
    ))

    # Herzfrequenzlinie für die linke Seite (y-Achse)
    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["HeartRate"],
        mode='lines',
        name='Herzfrequenz (bpm)',
        line=dict(color='red'),
        yaxis='y1'
    ))

    # Herzfrequenz-Zonen als Hintergrund
    zones = [
    {"min": 0.0,  "max": 0.6* max_hr, "color": "rgba(255, 255, 150, 0.3)", "name": "Zone 1"},
    {"min": 0.6*max_hr,  "max": 0.7* max_hr, "color": "rgba(200, 230, 100, 0.4)", "name": "Zone 2"},
    {"min": 0.7*max_hr,  "max": 0.8* max_hr, "color": "rgba(150, 200, 50, 0.5)",  "name": "Zone 3"},
    {"min": 0.8*max_hr,  "max": 0.9* max_hr, "color": "rgba(100, 160, 0, 0.6)",  "name": "Zone 4"},
    {"min": 0.9*max_hr,  "max": 1.0* max_hr, "color": "rgba(0, 100, 0, 0.7)",     "name": "Zone 5"},
    ]


    for zone in zones:
        fig.add_shape(
            type="rect",
            xref="paper",  # über die gesamte Breite
            yref="y1",     # an linke y-Achse gebunden (Herzfrequenz)
            x0=0,
            x1=1,
            y0=zone["min"],
            y1=zone["max"],
            fillcolor=zone["color"],
            line=dict(width=0),
            layer="below"
        )

         # Dummy-Trace zur Legende hinzufügen
        fig.add_trace(go.Scatter(
            x=[None], y=[None],  # Keine echten Punkte
            mode='markers',
            marker=dict(size=10, color=zone["color"]),
            name=zone["name"]
        ))


        fig.update_layout(
            title="Herzfrequenz & Leistung mit Herzfrequenzzonen",
            title_x=0.5,  # zentriert den Titel
            xaxis=dict(title="Zeit (s)"),
            yaxis=dict(
                title="Herzfrequenz (bpm)",
                side="left",
                showgrid=True,
                zeroline=False
            ),    
            yaxis2=dict(
                title="Leistung (Watt)",
                side="right",
                overlaying="y",
                showgrid=False,
                zeroline=False
            ),
            legend=dict(
                x=1.02,  # Rechts neben dem Plot
                y=1,
                orientation="v",
                xanchor="left"
            ),
            margin=dict(l=60, r=60, t=100, b=40)  # Mehr Platz oben für Titel
        )

    return fig




if __name__ == "__main__":
    df = read_my_csv()
    #print(df.head())
    fig = make_plot(df)
    fig.show()
    #add_heart_rate_zones(df, max_HR_person)
    print(load_data)


