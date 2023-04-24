import streamlit as st
import plotly.express as px
import pandas as pd
from code_schoof_algorithm import schoof_algorithm, points_on_curve, mod_inverse


def point_addition(P, Q, a, p):
    O = "O"

    if P == O:
        return Q
    if Q == O:
        return P

    x1, y1 = eval(P)  # Konvertieren Sie die Zeichenkette P in ein Tupel
    x2, y2 = eval(Q)  # Konvertieren Sie die Zeichenkette Q in ein Tupel

    if x1 == x2 and (y1 != y2 or y1 == 0):
        return O

    try:
        if P == Q:
            lam = (3 * x1 ** 2 + a) * mod_inverse(2 * y1, p) % p
        else:
            lam = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    except Exception:
        return O

    x3 = (lam ** 2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return f"({x3}, {y3})"  # Geben Sie das Ergebnis als Zeichenkette zurück


def draw_elliptic_curve(a, b, p):
    points = points_on_curve(a, b, p)
    data = pd.DataFrame(points, columns=["x", "y"])

    fig = px.scatter(data, x="x", y="y", title="Elliptische Kurve")
    return fig



def create_addition_table(a, b, p):
    O = "O"
    curve_points = list(points_on_curve(a, b, p))
    curve_points.sort(key=lambda point: (point[0], point[1]))
    points = [O] + [(f"({x}, {y})") for x, y in curve_points]
    addition_table = []

    for P in points:
        row = []
        for Q in points:
            if points.index(P) <= points.index(Q):
                row.append(point_addition(P, Q, a, p))
            else:
                row.append(point_addition(Q, P, a, p))
        addition_table.append(row)

    return pd.DataFrame(addition_table, columns=points, index=points)




st.title("Schoof-Algorithmus für elliptische Kurven")

a = st.number_input("Geben Sie den Koeffizienten a ein:", value=3)
b = st.number_input("Geben Sie den Koeffizienten b ein:", value=5)
p = st.number_input("Geben Sie den Primzahlmodul p ein:", value=11)

if st.button("Berechne Anzahl der Punkte und zeichne Kurve"):
    try:
        num_points = schoof_algorithm(a, b, p)
        st.write(f"Die Anzahl der Punkte auf der elliptischen Kurve ist: {num_points}")

        curve_plot = draw_elliptic_curve(a, b, p)
        st.plotly_chart(curve_plot)

        addition_table = create_addition_table(a, b, p)


        st.table(addition_table)


    except ValueError as e:
        st.error(f"Ein Fehler ist aufgetreten: {e}")
