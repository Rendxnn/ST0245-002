import pydeck as pdk
import pandas as pd


def plotMap():
    TRIPS_LAYER_DATA = "example.json"  # noqa

    df = pd.read_json(TRIPS_LAYER_DATA)

    df["coordinates"] = df["waypoints"].apply(lambda f: [item["coordinates"] for item in f])
    df["timestamps"] = df["waypoints"].apply(lambda f: [item["timestamp"] - 1554772579000 for item in f])

    df.drop(["waypoints"], axis=1, inplace=True)

    layer = pdk.Layer(
        "TripsLayer",
        df,
        get_path="coordinates",
        get_timestamps="timestamps",
        get_color=[253, 128, 93],
        opacity=0.8,
        width_min_pixels=5,
        rounded=True,
        trail_length=600,
        current_time=500,
    )

    view_state = pdk.ViewState(latitude=6.2115169, longitude=-75.5728593, zoom=11, bearing=0, pitch=45)

    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    r.to_html("trips_layer.html")