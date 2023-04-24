import streamlit as st
import matplotlib.pyplot as plt
from code_schoof_algorithm import schoof_algorithm, points_on_curve  # Importieren Sie die Funktionen aus Ihrem vorhandenen Code


def draw_elliptic_curve(a, b, p):
    points = points_on_curve(a, b, p)
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, color="blue")
    ax.set_title("Elliptische Kurve")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    return fig


st.title("Schoof-Algorithmus für elliptische Kurven")

a = st.number_input("Geben Sie den Koeffizienten a ein:", value=3)
b = st.number_input("Geben Sie den Koeffizienten b ein:", value=5)
p = st.number_input("Geben Sie den Primzahlmodul p ein:", value=11)

if st.button("Berechne Anzahl der Punkte und zeichne Kurve"):
    try:
        num_points = schoof_algorithm(a, b, p)
        st.write(f"Die Anzahl der Punkte auf der elliptischen Kurve ist: {num_points}")

        curve_plot = draw_elliptic_curve(a, b, p)
        st.pyplot(curve_plot)

    except ValueError as e:
        st.error(f"Ein Fehler ist aufgetreten: {e}")
