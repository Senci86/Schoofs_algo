def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_euclidean_algorithm(b % a, a)
        return g, y - (b // a) * x, x


def mod_inverse(a, m):
    g, x, _ = gcd_extended(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def elliptic_curve_add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 != y2 or y1 == 0):
        return None

    if P == Q:
        slope = (3 * x1 * x1 + a) * mod_inverse(2 * y1, p) % p
    else:
        slope = (y2 - y1) * mod_inverse(x2 - x1, p) % p

    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return x3, y3


def points_on_curve(a, b, p):
    points = set()
    for x in range(p):
        for y in range(p):
            if (y * y - x * x * x - a * x - b) % p == 0:
                points.add((x, y))
    return points


def schoof_algorithm(a, b, p):
    assert (4 * a ** 3 + 27 * b ** 2) % p != 0, "Die elliptische Kurve ist singulär"

    points = points_on_curve(a, b, p)
    points.add(None)

    N = len(points)

    return N


if __name__ == "__main__":
    a = int(input("Geben Sie den Koeffizienten a ein: "))
    b = int(input("Geben Sie den Koeffizienten b ein: "))
    p = int(input("Geben Sie den Primzahlmodul p ein: "))

    num_points = schoof_algorithm(a, b, p)
    print(f"Die Anzahl der Punkte auf der elliptischen Kurve ist: {num_points}")
