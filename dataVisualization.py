import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("starsChart.csv")
df.head()

star_mass = df["Mass"].to_list()
star_radius = df["Radius"].to_list()
star_distance = df["Distance"].to_list()
star_gravity = df["Gravity"].to_list()

star_mass.sort()
star_radius.sort()
star_gravity.sort()
star_distance.sort()

plt.plot(star_radius, star_mass)
plt.title("Radius vs. Mass of Stars (Line Plot)")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(star_mass, star_gravity)
plt.title("Mass vs. Gravity of Stars (Line Plot)")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

fig = px.scatter(x=star_radius, y=star_mass, 
                labels={
                    "x":"Radius",
                    "y":"Mass"
                }, title="Radius vs. Mass of Stars (Scatter Plot)")
fig.show()

fig = px.scatter(x=star_mass, y=star_gravity, size=star_radius,
                labels={
                    "x":"Mass",
                    "y":"Gravity"
                }, title="Mass vs. Gravity of Stars (Scatter Plot)")
fig.show()

fig = px.scatter_3d(x=star_mass, y=star_gravity, z=star_radius,
                    labels={
                        "x":"Mass",
                        "y":"Gravity",
                        "z":"Radius",
                    }, title="Overview of Stars")
fig.show()

