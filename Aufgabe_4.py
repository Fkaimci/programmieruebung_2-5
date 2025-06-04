import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("data/activities/activity.csv")
    return df["PowerOriginal"]

def best_effort(power_series, seconds):
    return power_series.rolling(window=seconds).mean().max()

def create_powercurve(power_series, durations):
    best_power = []
    for d in durations:
        if d <= len(power_series):
            best = best_effort(power_series, d)
            best_power.append(best)
        else:
            best_power.append(None)
    return pd.DataFrame({'duration': durations, 'best_efforts': best_power})

def plot_and_save_powercurve(df_curve):
    plt.figure(figsize=(10, 6))
    x_minutes = df_curve['duration'] / 60
    plt.plot(x_minutes, df_curve['best_efforts'], marker='o', color='royalblue')
    plt.xscale('log')

    # Manuelle Tick-Positionen auf der x-Achse (Minuten)
    ticks = [0.1, 0.2, 0.3, 1, 2, 3, 4, 5, 10, 20, 30]
    plt.xticks(ticks, [str(t) for t in ticks])

    plt.title('Power Curve')
    plt.xlabel('Dauer(min)')
    plt.ylabel('Leistung (Watt)')
    plt.grid(True, which="both", ls="--")
    plt.savefig('power_curve.png')
    plt.show()

if __name__ == "__main__":
    durations = [5, 10, 15, 20, 30, 45, 60, 90, 120, 180, 240, 300, 600, 900, 1200, 1800]
    power_series = load_data()
    print(f"Anzahl Power-Datenpunkte: {len(power_series)}")
    power_curve_df = create_powercurve(power_series, durations)
    print(power_curve_df)
    plot_and_save_powercurve(power_curve_df)

