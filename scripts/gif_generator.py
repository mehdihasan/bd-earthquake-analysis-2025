import imageio.v2 as imageio
import pandas as pd
import plotly.express as px
import os

frames = []

df = pd.read_csv('data/query.csv')
df.info()
df['time'] = pd.to_datetime(df['time'], errors='coerce')

# Extract year for temporal analysis
df['year'] = df['time'].dt.year
min_lat, max_lat = 20.0, 26.9
min_lon, max_lon = 87.5, 93.0

region_df = df[
    (df['latitude'].between(min_lat, max_lat)) &
    (df['longitude'].between(min_lon, max_lon))
].copy()

# Loop over all animation frames by year
years = sorted(region_df["year"].unique())

for year in years:
    temp_df = region_df[region_df["year"] == year].copy()
    temp_df["label"] = temp_df.apply(
        lambda r: f"M{r.mag:.1f} {r.depth}km", axis=1
    )

    temp_df["size"] = temp_df["mag"] * 6  # scale circles by magnitude

    fig_year = px.scatter_geo(
        temp_df,
        lat="latitude",
        lon="longitude",
        size="size",
        color="mag",
        text="label",
        hover_name="place",
        projection="natural earth",
        title=f"betweensystems.com   Earthquakes - {year}",
        color_continuous_scale="Turbo",

        # ★ Fixed color scale
        range_color=[2.5, 8],
    )

    fig_year.update_traces(
        textposition="middle center",
        textfont=dict(
            family="Arial",
            size=10,          # Adjust depending on circle size
            color="black"     # or darker color for better contrast
        ),
        marker=dict(
            line=dict(width=0.5, color="black"),
            sizemin=3,
            opacity=0.85,
        )
    )

    # ★ Fixed window (does not move)
    fig_year.update_geos(
        showcountries=True,
        showland=True,
        landcolor="#e8e6d9",
        oceancolor="#c9e6ff",
        showocean=True,
        showsubunits=True,
        projection_type="natural earth",
        lonaxis_range=[min_lon, max_lon],
        lataxis_range=[min_lat, max_lat],
    )

    file = f"frame_{year}.png"
    fig_year.write_image(file, scale=2, width=1000, height=800)
    frames.append(imageio.imread(file))

# Generate GIF
imageio.mimsave("earthquake_animation.gif", frames, fps=0.50)

# Cleanup PNGs
for f in os.listdir():
    if f.startswith("frame_") and f.endswith(".png"):
        os.remove(f)

print("GIF saved as earthquake_animation.gif")
