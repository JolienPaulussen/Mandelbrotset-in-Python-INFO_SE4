mport numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    In deze functie wordt de Mandelbrot formule uitgerekend.
    param: c (complex) het complexe getal waarvoor je de formule uitrekent.
    param: max_iter (integer) het maximale aantal dat je de formule mag uitrekenen
        om uit te proberen of de Mandelbrot formule begrenst is voor dat complexe getal (= 80).
    :return: (integer) een getal tussen 0 en max_iter (= 80).
    """
    z = complex(0, 0)
    for n in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return n
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    """
    In deze functie wordt de Mandelbrotset gemaakt.
    param: xmin (float) de laagste waarde van de x-as (= -2.0).
    param: xmax (float) de hoogste waarde van de x-as (= o.5).
    param: ymin (float) de laagste waarde van de y-as (= -1.25).
    param: ymax (float) de hoogste waarde van de y-as (= 1.25).
    param: width (integer) het aantal punten van de x-as (= 1000).
    param: height (integer) het aantal punten van de y-as (= 1000).
    param: maxiter (integer) het maximale aantal dat je de formule mag uitrekenen
        om uit te proberen of de mandelbrot formule begrenst is voor dat complexe getal (= 80).
    :return: (tuple) het x-as-object en het y-as-object gevolgd door een lijst met alle punten van het rooster.
    """
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    lijst = []
    for r in r1:
        for i in r2:
            lijst.append(mandelbrot(complex(r, i), maxiter))                    
    return (r1, r2, lijst)


def plot(m_set):
    """
    Deze functie zet de Mandelbrotset om in een grafische weergave.
    param: m_set (tuple) het x-as-object en het y-as-object gevolgd door een lijst met alle punten van het rooster.
    :return: None. Maar er verschijnt wel een venster met een plaatje.
    """
    x_as, y_as, lst = m_set
    realAxisLen = len(x_as)
    imaginaryAxisLen = len(y_as)
    
    # Een 2 dimensionaal array dat een Mandelbrotset representeert.
    rooster = np.empty((realAxisLen, imaginaryAxisLen))

    for x in xrange(realAxisLen):
        for y in xrange(imaginaryAxisLen):
            rooster[x, y] = lst[x * realAxisLen + y]

    # Hier wordt een plaatje gemaakt met het 2 dimensionaal array.
    fig, ax = plt.subplots()
    ax.imshow(rooster.T, interpolation="nearest", origin='upper')
    plt.show()

def translate(point, amount):
    """
    In deze functie wordt een translatie uitgevoerd op een punt.
    param: point (float) een punt op een as.
    param: amount (float) een bepaalde hoeveelheid die je bij het punt optelt.
    :return: (float) het verplaatste punt.
    """
    return point+amount

def zoom(min, max, factor):
    """
    In deze functie wordt het in- en uitzoomen geregeld.
    param: min (float) het huidige minimum van de as waarover je wil inzoomen.
    param: max (float) het huidige maximum van de as waarover je wil inzoomen.
    param: factor (float) de factor waarmee je wil inzoomen.
        Als die groter is dan 1, dan zoom je in.
        Als die kleiner is dan 1, dan zoom je uit.
    :return: (tuple) het nieuwe minimum en het nieuwe maximum van de as.
    """
    return min/factor, max/factor

print("START")

# Hier wordt de grafische weergave van de Mandelbrotset gemaakt. Dit is het startpunt van het programma.
# Ook wordt er hier voor gezorgd dat er kan worden ingezoomd.
for zoom_factor in range(1, 50, 2):
    y_as = zoom(translate(-1.25, zoom_factor-1), translate(1.25, zoom_factor-1), zoom_factor)
    x_as = zoom(translate(-2.00, -1 * (zoom_factor - 1) / 10), translate(0.50, -1 * (zoom_factor - 1) / 10), zoom_factor)
    plot(mandelbrot_set(x_as[0], x_as[1], y_as[0], y_as[1], 1000, 1000, 80))

print("KLAAR")
