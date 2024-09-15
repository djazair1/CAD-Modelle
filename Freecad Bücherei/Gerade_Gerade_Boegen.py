import FreeCAD
import FreeCADGui
import Part
import Draft
import App
import FreeCAD
import requests
print("HUND")
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Lamelle_real.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Lamelle_real.FCStd", "wb") as f:
    f.write(r.content)
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_weg_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_weg_horizontal.FCStd", "wb") as f:
    f.write(r.content)
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_weg_horizontal.FCStd"
################
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_vertikal_weg.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_vertikal_weg.FCStd", "wb") as f:
    f.write(r.content)
###############
# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_weg_horizontal.FCStd", "wb") as f:
    f.write(r.content)
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_vertikal_hin.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_vertikal_hin.FCStd", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

#######################################################
url ="https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Lamelle_real_15.FCStd"
r = requests.get(url)
with open("Lamelle_real_15.FCStd", "wb") as f:
    f.write(r.content)
#######################################################
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Blech_12.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Blech_12.FCStd", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

#######################################################
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_quer_hin_links.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_quer_hin_links.FCStd", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

#############
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_quer_hin_rechts.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_quer_hin_rechts.FCStd", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

#######
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_quer_weg_links.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_quer_weg_links", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

###
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_quer_weg_rechts.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_quer_weg_rechts", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

###############################
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_hin_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_hin_horizontal", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

############################################
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_hin_horizontal_springer.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_hin_horizontal_springer", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

############
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_weg_horizontal.20240217-190845.FCBak"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_weg_horizontal.20240217-190845", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_weg_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_weg_horizontal", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_weg_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_weg_horizontal", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_vertikal_hin.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_vertikal_hin", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_weg_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_weg_horizontal", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_vertikal_hin_springer.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_vertikal_hin_springer", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_weg_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_weg_horizontal", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_vertikal_weg.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_vertikal_weg", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_vertikal_weg_springer.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_vertikal_weg_springer", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_weg_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_weg_horizontal", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_weg_horizontal_springer.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_weg_horizontal_springer", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/B%C3%B6gen_12.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("B%C3%B6gen_12.FCStd", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/B%C3%B6gen_memo.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("B%C3%B6gen_memo.FCStd", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Lamelle_15.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Lamelle_15.FCStd", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Lamelle_plan.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Lamelle_plan", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Lamelle_real.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Lamelle_real", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Lamelle_real_15.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Lamelle_real_15", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Bogen_unten_weg_horizontal.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Bogen_unten_weg_horizontal", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen
###########
url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Langer_bogen.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Langer_bogen", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Spreadsheet.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Spreadsheet", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Langer_bogen.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Langer_bogen", "wb") as f:
    f.write(r.content)

# In FreeCAD öffnen

url = "https://github.com/djazair1/CAD-Modelle/raw/main/Freecad%20B%C3%BCcherei/Spreadsheet_v2.FCStd"

# Datei herunterladen und direkt als "Unnamed.FCStd" speichern
r = requests.get(url)
with open("Spreadsheet_v2", "wb") as f:
    f.write(r.content)



import FreeCAD
def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False
doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)
Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
#SCHLEIFE DER MASSEN
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    import FreeCAD
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_hin.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_hin').getObject('AdditivePipe'), True)
    anderes_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_dokument_name)
    import FreeCAD
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_unten_hin_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_unten_hin_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_hin_vertikal = "AdditivePipe"
    original_body = App.ActiveDocument.getObject(Bogen_hin_vertikal)
    # Überprüfen, ob der Körper existiert
    if original_body:
        # Ihr Spreadsheet und der Alias-Name
        spreadsheet_name = "Spreadsheet"
        alias_name = "Rohr_hoehe"

        # Holen Sie den Wert aus dem Spreadsheet
        try:
            doc = App.activeDocument()
            spreadsheet = doc.getObject(spreadsheet_name)
            height_value = spreadsheet.get(alias_name)
        except Exception as e:
            App.Console.PrintError(f"Fehler beim Abrufen des Werts: {e}")

        # Teilen Sie den Wert durch 0,5 und berechnen Sie die Anzahl der Punkte
        num_points = Rohr_hoehe_value / 2

        # Abstand zwischen den Punkten
        spacing = Rohrabstand_value * 2

        # Initialer Y-Wert für den ersten Punkt
        initial_y = Rohrabstand_value / 2

        # Berechnen Sie die Punkte
        points = draw_points(num_points, spacing, initial_y)

        # Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
        add_AdditivePipe(points, original_body)
        for i in range(1, Rohr_breite_value - 2):
            x_offset = Rohrabstand_value * i
            add_AdditivePipe(points, original_body, x_offset)

        App.Console.PrintMessage(f"{num_points} Punkte wurden in Y-Richtung mit einem Abstand von {spacing} gezeichnet. Der erste Punkt hat den Y-Wert 17,5.")
        App.Console.PrintMessage(f"Das Skript wurde 4 Mal in X-Richtung verschoben, jeweils um 40 Einheiten.")
    else:
        print("Nein")
else:
    print("unter 2 oder 2")
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    Bogen_hin_horizontal = "AdditivePipe001"
    original_body_1 = App.ActiveDocument.getObject(Bogen_hin_horizontal)
    Num_points_1 = Rohr_hoehe_value
    spacing_1 = Rohrabstand_value
    initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = (Rohr_breite_value-1)* Rohrabstand_value - (Rohrabstand_value/2)  # Setzen Sie den x_offset-Wert entsprechend Ihren Anforderungen
    add_AdditivePipe(points_1, original_body_1, x_offset)
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False
doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)
Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def add_AdditivePipe(points, original_body, x_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_vertikal= "AdditivePipe002"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_vertikal)
    Num_points_1 =(Rohr_hoehe_value - 1) * 0.5
    spacing_1 = Rohrabstand_value * 2
    initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1,original_body_weg_1, x_offset, z_offset)
    for i in range(Rohr_breite_value - 2):
        Bogen_weg_vertikal = "AdditivePipe002"
        original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = (Rohr_hoehe_value - 1) * 0.5
        spacing_1 = Rohrabstand_value * 2
        initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
        add_AdditivePipe(points_1, original_body_weg_1, x_offset, z_offset)
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_x):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_x, y_value):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(x_value, y_value, 0))  
    return points
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, y_offset, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_weg_horizontal= "AdditivePipe003"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_horizontal)
    Num_points_1 = (Rohr_breite_value - 2) / 2 
    spacing_1 = Rohrabstand_value * 2
    initial_x = Rohrabstand_value /  2   # Hier setzen Sie den Anfangswert für die Y-Position
    y_value = (Rohr_hoehe_value - 1) * Rohrabstand_value # Setzen Sie hier den gewünschten y-Wert ein
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
    x_offset = 0
    y_offset = 0  # Set the desired y offset here
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg_1, x_offset, y_offset, z_offset)
    draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_weg_horizontal= "AdditivePipe003"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_horizontal)
    Num_points_1 = (Rohr_breite_value - 2) / 2 
    spacing_1 = Rohrabstand_value * 2
    initial_x = Rohrabstand_value * 1.5   # Hier setzen Sie den Anfangswert für die Y-Position
    y_value = 0 # Setzen Sie hier den gewünschten y-Wert ein
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
    x_offset = 0
    y_offset = 0  # Set the desired y offset here
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg_1, x_offset, y_offset, z_offset)

    draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Oben_rechts_H_cell = spreadsheet.Oben_rechts_H
Oben_rechts_H_value = str(Oben_rechts_H_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_x):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_x, y_value):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(x_value, y_value, 0))  
    return points
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, y_offset, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
def add_AdditivePipe_1(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


import FreeCAD

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_unten_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_unten_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe002"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = Rohrabstand_value * 1.5
    initial_x = (Rohr_breite_value - 2) * Rohrabstand_value
    y_offset = Rohrabstand_value * 2 
    num_copies = (Rohr_hoehe_value - 2) / 2
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x, initial_y + i * y_offset, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
    App.ActiveDocument.recompute()

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe002"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = Rohrabstand_value / 2 
    initial_x = (Rohr_breite_value - 1) * Rohrabstand_value
    y_offset = Rohrabstand_value * 2
    num_copies = (Rohr_hoehe_value - 2) / 2
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x, initial_y + i * y_offset, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
        y_offset = Rohrabstand_value * 2 
    App.ActiveDocument.recompute()


import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_x):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_x, y_value):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(x_value, y_value, 0))  
    return points
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, y_offset, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
def add_AdditivePipe_1(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


import FreeCAD

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_quer_weg_links.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_quer_weg_links').getObject('AdditivePipe'), True)
    Bogen_quer_hin_links_1 = 'AdditivePipe005'
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    import FreeCAD
    mein_objekt = App.ActiveDocument.getObject(Bogen_quer_hin_links_1)
    new_x = (Rohr_breite_value - 1.5) * Rohrabstand_value
    new_y = (Rohr_hoehe_value - 1.5) * Rohrabstand_value
    new_z = Rohrlaenge_value
    Placement = mein_objekt.Placement
    new_placement = FreeCAD.Placement(mein_objekt.Placement)
    new_placement.Base = FreeCAD.Vector(new_x, new_y, new_z)
    mein_objekt.Placement = new_placement

# Dokument aktualisieren
App.ActiveDocument.recompute()
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
 FreeCAD.ActiveDocument.removeObject("AdditivePipe")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe001")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe002")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe003")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe004")
import FreeCAD
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
 def delete_documents_except_unnamed():
    # Überprüfen, ob das Dokument aktiv ist
    if FreeCAD.ActiveDocument is None:
        print("Es gibt kein aktives Dokument.")
        return

    # Durchlaufen aller geöffneten Dokumente
    for document_name in FreeCAD.listDocuments():
        if document_name != "Unnamed":
            FreeCAD.closeDocument(document_name)
            print("Das Dokument '{}' wurde erfolgreich geloscht.".format(document_name))
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
# Aufruf der Funktion zum Löschen aller Dokumente außer "Unnamed"
 delete_documents_except_unnamed()
 import FreeCAD
 anderes_memo_dokument_name = "Unnamed"
 FreeCAD.setActiveDocument(anderes_memo_dokument_name)
def delete_all_planes():
    # Überprüfen, ob das Dokument aktiv ist
    if FreeCAD.ActiveDocument is None:
        print("Es gibt kein aktives Dokument.")
        return

    # Durchlaufen aller Objekte im aktiven Dokument
    for obj in FreeCAD.ActiveDocument.Objects:
        # Überprüfen, ob das Objekt ein Plane ist
        if obj.TypeId == 'PartDesign::Plane':
            # Objekt löschen
            FreeCAD.ActiveDocument.removeObject(obj.Name)
            print("Die Ebene '{}' wurde erfolgreich gelöscht.".format(obj.Label))

# Aufruf der Funktion zum Löschen aller Ebenen im aktiven Dokument

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value > 2:
  delete_all_planes()
import FreeCAD as App

doc = App.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_links_V_cell = spreadsheet.Oben_links_V
Oben_links_V_value = str(Oben_links_V_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)


def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False


def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point + App.Vector(x_offset + initial_x, y_offset, z_offset)
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point.add(App.Vector(x_offset + initial_x, y_offset, z_offset))
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

# Call the function with the corrected arguments
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_vertikal_hin = "AdditivePipe"
    original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
    Num_points_1 = Rohr_hoehe_value 
    spacing_1 = Rohrabstand_value
    initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0   # Passen Sie diesen Wert nach Bedarf an
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    initial_x = Rohrabstand_value * 1.5   # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)
    Range_wert = int(Rohr_breite_value / 2 - 2)
    for i in range(Range_wert):
        Bogen_weg_vertikal = "AdditivePipe"
        initial_x = Rohrabstand_value * 3.5
        original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = Rohr_hoehe_value 
        spacing_1 = Rohrabstand_value 
        initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * 2 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)
import FreeCAD as App

doc = App.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_links_V_cell = spreadsheet.Oben_links_V
Oben_links_V_value = str(Oben_links_V_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)


def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False


def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point + App.Vector(x_offset + initial_x, y_offset, z_offset)
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value > 2:
   FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg.FCStd")
   App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg').getObject('AdditivePipe'), True)
   anderes_bogen_dokument_name = "Unnamed"
   FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
   Bogen_vertikal_hin = "AdditivePipe001"
   original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
   num_points = int(Rohr_hoehe_value / 2 - 1)
   spacing = Rohrabstand_value * 2 
   initial_y = Rohrabstand_value * 1.5 
   initial_x = 0
   x_offset = 0
   z_offset = Rohrlaenge_value
   points = create_points(num_points, spacing, initial_y, initial_x)
   create_pipes(points, original_body_weg, x_offset, z_offset, initial_x)


if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value > 2:
   num_points = int(Rohr_hoehe_value / 2)
   spacing = Rohrabstand_value * 2 
   initial_y = Rohrabstand_value / 2  
   initial_x = 0
   x_offset = int((Rohr_breite_value -1)* Rohrabstand_value)
   z_offset = Rohrlaenge_value
   points = create_points(num_points, spacing, initial_y, initial_x)
   create_pipes(points, original_body_weg, x_offset, z_offset, initial_x)
   


import FreeCAD as App

doc = App.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_links_V_cell = spreadsheet.Oben_links_V
Oben_links_V_value = str(Oben_links_V_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)


def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False


def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point + App.Vector(x_offset + initial_x, y_offset, z_offset)
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy

# Call the function with the corrected arguments
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_unten_hin_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_unten_hin_horizontal').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_vertikal_hin = "AdditivePipe002"
    original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
    Num_points_1 = Rohr_hoehe_value 
    spacing_1 = Rohrabstand_value
    initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0   # Passen Sie diesen Wert nach Bedarf an
    z_offset = 0  # Passen Sie diesen Wert nach Bedarf an
    initial_x = Rohrabstand_value * 0.5  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)
    Range_wert = int(Rohr_breite_value / 2 - 1)
    for i in range(Range_wert):
        Bogen_weg_vertikal = "AdditivePipe002"
        initial_x = Rohrabstand_value * 2.5
        original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = Rohr_hoehe_value 
        spacing_1 = Rohrabstand_value 
        initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * 2 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)


if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value > 2:
 FreeCAD.ActiveDocument.removeObject("AdditivePipe")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe001")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe002")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe003")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe004")


import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)

#Nicht vergessen if command beenden #Nicht vergessen if command beenden #Nicht vergessen if command beenden #Nicht vergessen if command beenden 
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = (Rohr_hoehe_value - 1) * Rohrabstand_value
    initial_x = Rohrabstand_value / 2 
    x_offset = Rohrabstand_value * 2 
    num_copies = Rohr_breite_value / 2 
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    
    # Hier können Sie den horizontalen Abstand zwischen den Objekten festlegen
    x_between_objects = Rohrabstand_value * 2   # Beispielwert, ändern Sie dies entsprechend Ihrer Anforderungen
    
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x + i * x_between_objects, initial_y, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
 

def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
    App.ActiveDocument.recompute()



   
    App.ActiveDocument.recompute()
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = 0
    initial_x = Rohrabstand_value * 1.5 
    x_offset = Rohrabstand_value * 2
    num_copies = Rohr_breite_value / 2 - 1
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    
    # Hier konnen Sie den horizontalen Abstand zwischen den Objekten festlegen
    x_between_objects = Rohrabstand_value * 2 # Beispielwert, ändern Sie dies entsprechend Ihrer Anforderungen
    
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x + i * x_between_objects, initial_y, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
    
    App.ActiveDocument.recompute()
#Nicht vergessen if command beenden #Nicht vergessen if command beenden #Nicht vergessen if command beenden #Nicht vergessen if command beenden 
import FreeCAD as App
import Part

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_V_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_vertikal = "AdditivePipe001"
    original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
    Num_points_1 = (Rohr_hoehe_value - 1) * 0.5
    spacing_1 = Rohrabstand_value * 2
    initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg, x_offset, z_offset)
    for i in range(Rohr_breite_value):
        Bogen_weg_vertikal = "AdditivePipe001"
        original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = (Rohr_hoehe_value - 1) * 0.5
        spacing_1 = Rohrabstand_value * 2
        initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = 35 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        add_AdditivePipe(points_1, original_body_weg, x_offset, z_offset)
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)

def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
    App.ActiveDocument.recompute()

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_V_value == "X" and Rohr_hoehe_value > 2:
  FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_hin.FCStd")
  App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_hin').getObject('AdditivePipe'), True)
  anderes_bogen_dokument_name = "Unnamed"
  FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
  Bogen_vertikal_hin = "AdditivePipe002"
  original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
  Num_points_1 = Rohr_hoehe_value / 2
  spacing_1 = Rohrabstand_value * 2
  initial_y = 0.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
  points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
  x_offset = 0 # Passen Sie diesen Wert nach Bedarf an
  add_AdditivePipe(points_1, original_body_weg, x_offset)
  for i in range(Rohr_breite_value):
   Bogen_weg_vertikal = "AdditivePipe002"
   original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
   Num_points_1 = Rohr_hoehe_value / 2
   spacing_1 = Rohrabstand_value * 2
   initial_y = Rohrabstand_value / 2  # Hier setzen Sie den Anfangswert für die Y-Position
   points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
   x_offset = Rohrabstand_value * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
   add_AdditivePipe(points_1, original_body_weg, x_offset)

  # Dokument aktualisieren
App.ActiveDocument.recompute()
import FreeCAD as App

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False
doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet

Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell=spreadsheet.Rohrabstand
Rohrabstand_value=int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value == 2:
 App.Console.PrintMessage("Bedingungen erfüllt. Das Skript wird ausgeführt.\n")
 FreeCAD.openDocument('C:/Users/jamin/OneDrive/Desktop/Freecad B\xfccherei/Bogen_vertikal_hin.FCStd')
 App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_hin').getObject('AdditivePipe'), True)
 FreeCAD.openDocument('C:/Users/jamin/OneDrive/Desktop/Freecad B\xfccherei/Bogen_weg_horizontal.FCStd')
 App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
else:
 print("geht nicht")

import FreeCAD as App

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(num_points):
        y_value = initial_y + i * spacing
        points.append(App.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
# Macro Begin: C:\Users\jamin\AppData\Roaming\FreeCAD\Macro\Hustllaaaaa.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD

anderes_dokument_name = "Unnamed"

# Überprüfen, ob das Dokument existiert
if FreeCAD.getDocument(anderes_dokument_name):
    # Setze das andere Dokument als aktives Dokument
    FreeCAD.setActiveDocument(anderes_dokument_name)
    # Aktualisiere die Ansicht
    FreeCAD.ActiveDocument.recompute()
# Hauptskript
def main():
    doc = FreeCAD.ActiveDocument
    spreadsheet = doc.Spreadsheet

    Rohrlaenge_cell = spreadsheet.Rohrlaenge
    Rohrlaenge_value = int(Rohrlaenge_cell)

    Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
    Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
    Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
    Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
    Rohrabstand_cell=spreadsheet.Rohrabstand
    Rohrabstand_value=int(Rohrabstand_cell)

    Oben_links_H_cell = spreadsheet.Oben_links_H
    Oben_links_H_value = str(Oben_links_H_cell)
    Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
    Oben_rechts_V_value = str(Oben_rechts_V_cell)
    Unten_links_V_cell = spreadsheet.Unten_links_V
    Unten_links_V_value = str(Unten_links_V_cell)
    Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
    Unten_rechts_V_value = str(Unten_rechts_V_cell)

    Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
    Rohr_hoehe_value = int(Rohr_hoehe_cell)
    Rohr_breite_cell = spreadsheet.Rohr_breite
    Rohr_breite_value = int(Rohr_breite_cell)

    if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value == 2:
        App.Console.PrintMessage("Bedingungen erfüllt. Das Skript wird ausgeführt.\n")

        Lamelle1x = "AdditivePipe"

        # Annahme: Der Körper, den Sie kopieren möchten, ist im Dokument vorhanden
        original_body = App.ActiveDocument.getObject(Lamelle1x)

        # Überprüfen, ob der Körper existiert
        if original_body:
            # Ihr Spreadsheet und der Alias-Name
            spreadsheet_name = "Spreadsheet"
            alias_name = "Rohr_hoehe"

            # Holen Sie den Wert aus dem Spreadsheet
            try:
                doc = App.activeDocument()
                spreadsheet = doc.getObject(spreadsheet_name)
                height_value = spreadsheet.get(alias_name)
            except Exception as e:
                App.Console.PrintError(f"Fehler beim Abrufen des Werts: {e}")
                return

            # Teilen Sie den Wert durch 0,5 und berechnen Sie die Anzahl der Punkte
            num_points = int(height_value * 0.5)

            # Abstand zwischen den Punkten
            spacing = Rohrabstand_value * 2

            # Initialer Y-Wert für den ersten Punkt
            initial_y = Rohrabstand_value / 2

            # Berechnen Sie die Punkte
            points = draw_points(num_points, spacing, initial_y)

            # Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
            add_AdditivePipe(points, original_body)

            # Kopieren und verschieben Sie das Skript 4 Mal in X-Richtung
            for i in range(1, Rohr_breite_value):
                x_offset =  Rohrabstand_value * i
                add_AdditivePipe(points, original_body, x_offset)

            App.Console.PrintMessage(f"{num_points} Punkte wurden in Y-Richtung mit einem Abstand von {spacing} gezeichnet. Der erste Punkt hat den Y-Wert 17,5.")
            App.Console.PrintMessage(f"Das Skript wurde 4 Mal in X-Richtung verschoben, jeweils um 40 Einheiten.")

    else:
        App.Console.PrintMessage("Bedingungen nicht erfüllt. Das Skript wird nicht ausgeführt.\n")

if __name__ == "__main__":
    main()

import FreeCAD as App 

doc = App.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)

Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)

Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value == 2:

 # Funktion zum Hinzufügen des kopierten Objekts an den berechneten Positionen
 def add_copied_objects(original_object, num_copies):
    copies = []
    for i in range(num_copies):
        copy = original_object.Shape.copy()
        x_offset = Rohrabstand_value * 1.5  + i * Rohrabstand_value * 2
        z_offset = Rohrlaenge_value
        copy.Placement.Base.x = x_offset
        copy.Placement.Base.z = z_offset
        copies.append(copy)
    return copies

 # Funktion zum Hinzufügen des kopierten Objekts an den berechneten Positionen
 def add_copied_objects_2(original_object, num_copies):
    copies = []
    for i in range(num_copies):
        copy = original_object.Shape.copy()
        x_offset = (Rohrabstand_value / 2) + i * Rohrabstand_value * 2
        z_offset = Rohrlaenge_value
        y_offset = Rohr_hoehe_value * Rohrabstand_value - Rohrabstand_value  # Setzen Sie den Y-Wert auf 35
        copy.Placement.Base.x = x_offset
        copy.Placement.Base.z = z_offset
        copy.Placement.Base.y = y_offset
        copies.append(copy)
    return copies

 # Hauptskript
 def main():
    # Annahme: Der Alias-Name ist bereits in einer Variable gespeichert
    Lamelle1x = "AdditivePipe001"

    # Holen Sie das vorhandene Objekt anhand des Alias-Namens
    original_object = App.ActiveDocument.getObject(Lamelle1x)

    # Überprüfen, ob das Objekt existiert
    if original_object:
        # Berechnen Sie die Anzahl der Kopien
        num_copies = (Rohr_breite_value - 2) // 2

        # Hinzufügen der kopierten Objekte an den berechneten Positionen
        copied_objects = add_copied_objects(original_object, num_copies)

        # Hinzufügen der kopierten Objekte zum Dokument
        for i, copy in enumerate(copied_objects, start=1):
            App.ActiveDocument.addObject("Part::Feature", f"Bogen_vorne_Copy_{i}").Shape = copy

        App.Console.PrintMessage(f"{num_copies} Kopien wurden erstellt und positioniert.")
    else:
        App.Console.PrintError("Das Objekt mit dem angegebenen Alias-Namen existiert nicht.")

    if original_object:
        # Berechnen Sie die Anzahl der Kopien
        num_copies = (Rohr_breite_value - 2) // 2

        # Hinzufügen der kopierten Objekte an den berechneten Positionen
        copied_objects = add_copied_objects_2(original_object, num_copies)

        # Hinzufügen der kopierten Objekte zum Dokument
        for j, copy in enumerate(copied_objects, start=1):
            App.ActiveDocument.addObject("Part::Feature", f"Bogen_vorne_Copy_{j}").Shape = copy

        App.Console.PrintMessage(f"{num_copies} Kopien wurden erstellt und positioniert.")
    else:
        App.Console.PrintError("Das Objekt mit dem angegebenen Alias-Namen existiert nicht.")
if __name__ == "__main__":
    main()
else:
        App.Console.PrintMessage("Bedingungen nicht erfüllt. Das Skript wird nicht ausgeführt.\n")

# Annahme: Der Name des anderen Dokuments ist "MeinAnderesDokument"
anderes_dokument_name = "Unnamed"

# Überprüfen, ob das Dokument existiert
if FreeCAD.getDocument(anderes_dokument_name):
    # Setze das andere Dokument als aktives Dokument
    FreeCAD.setActiveDocument(anderes_dokument_name)
    # Aktualisiere die Ansicht
    FreeCAD.ActiveDocument.recompute()
    print(f"{anderes_dokument_name} ist jetzt das aktive Dokument.")
else:
    print(f"Dokument mit dem Namen {anderes_dokument_name} nicht gefunden.")

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_V_value == "X" and Rohr_hoehe_value == 2:
 import FreeCAD
 FreeCAD.openDocument('C:/Users/jamin/OneDrive/Desktop/Freecad B\xfccherei/Bogen_quer_weg_links.FCStd')
 App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_quer_weg_links').getObject('AdditivePipe'), True)
 anderes_dokument_name = "Unnamed"

# Überprüfen, ob das Dokument existiert
 if FreeCAD.getDocument(anderes_dokument_name):
    # Setze das andere Dokument als aktives Dokument
    FreeCAD.setActiveDocument(anderes_dokument_name)
    # Aktualisiere die Ansicht
    FreeCAD.ActiveDocument.recompute()
    print(f"{anderes_dokument_name} ist jetzt das aktive Dokument.")
 else:
    print(f"Dokument mit dem Namen {anderes_dokument_name} nicht gefunden.")

 import FreeCAD as App
 import Part

# Name des gewünschten Objekts
 obj_name = "AdditivePipe002"

# Holen Sie das Dokument und das gewünschte Objekt
 doc = App.activeDocument()
 obj = doc.getObject(obj_name)

 if obj:
    # Aktuelle Position und Rotation ausgeben
    print("Aktuelle Position:", obj.Placement.Base)
    print("Aktuelle Rotation um Z-Achse:", obj.Placement.Rotation.toEuler()[2])

    # Neue Position und Rotation festlegen
    new_position = App.Vector(Rohrabstand_value*Rohr_breite_value-Rohrabstand_value*1.5, Rohrabstand_value / 2, Rohrlaenge_value)  # Beispielwerte für x, y, z
    rotation_angle = 45  # Beispielwert für den Drehwinkel in Grad

    # Mittelpunkt des Objekts
    center_point = obj.Shape.BoundBox.Center

    # Neue Platzierung erstellen
    new_placement = App.Placement(center_point, App.Rotation(App.Vector(0, 0, 1), rotation_angle))

    # Position des Objekts aktualisieren
    new_placement.Base = new_position

    # Platzierung des Objekts aktualisieren
    obj.Placement = new_placement

    # Neue Position und Rotation ausgeben
    print("Neue Position:", obj.Placement.Base)
    print("Neue Rotation um Z-Achse:", obj.Placement.Rotation.toEuler()[2])
else:
    print(f"Objekt mit dem Namen wurde nicht gefunden.")
import FreeCAD as App

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False
doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet

Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell=spreadsheet.Rohrabstand
Rohrabstand_value=int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_V_value == "X" and Rohr_hoehe_value == 2:
 App.Console.PrintMessage("Bedingungen erfüllt. Das Skript wird ausgeführt.\n")
 import FreeCAD
 FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_hin.FCStd")
 App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_hin').getObject('AdditivePipe'), True)
 FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
 App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
else:
 print("geht nicht")

import FreeCAD as App

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(num_points):
        y_value = initial_y + i * spacing
        points.append(App.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
# Macro Begin: C:\Users\jamin\AppData\Roaming\FreeCAD\Macro\Hustllaaaaa.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD

anderes_dokument_name = "Unnamed"

# Überprüfen, ob das Dokument existiert
if FreeCAD.getDocument(anderes_dokument_name):
    # Setze das andere Dokument als aktives Dokument
    FreeCAD.setActiveDocument(anderes_dokument_name)
    # Aktualisiere die Ansicht
    FreeCAD.ActiveDocument.recompute()
# Hauptskript
def main():
    doc = FreeCAD.ActiveDocument
    spreadsheet = doc.Spreadsheet

    Rohrlaenge_cell = spreadsheet.Rohrlaenge
    Rohrlaenge_value = int(Rohrlaenge_cell)

    Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
    Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
    Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
    Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
    Rohrabstand_cell=spreadsheet.Rohrabstand
    Rohrabstand_value=int(Rohrabstand_cell)

    Oben_links_H_cell = spreadsheet.Oben_links_H
    Oben_links_H_value = str(Oben_links_H_cell)
    Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
    Oben_rechts_V_value = str(Oben_rechts_V_cell)
    Unten_links_V_cell = spreadsheet.Unten_links_V
    Unten_links_V_value = str(Unten_links_V_cell)
    Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
    Unten_rechts_V_value = str(Unten_rechts_V_cell)

    Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
    Rohr_hoehe_value = int(Rohr_hoehe_cell)
    Rohr_breite_cell = spreadsheet.Rohr_breite
    Rohr_breite_value = int(Rohr_breite_cell)

    if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_V_value == "X" and Rohr_hoehe_value == 2:
        App.Console.PrintMessage("Bedingungen erfüllt. Das Skript wird ausgeführt.\n")

        Lamelle1x = "AdditivePipe"

        # Annahme: Der Körper, den Sie kopieren möchten, ist im Dokument vorhanden
        original_body = App.ActiveDocument.getObject(Lamelle1x)

        # Überprüfen, ob der Körper existiert
        if original_body:
            # Ihr Spreadsheet und der Alias-Name
            spreadsheet_name = "Spreadsheet"
            alias_name = "Rohr_hoehe"

            # Holen Sie den Wert aus dem Spreadsheet
            try:
                doc = App.activeDocument()
                spreadsheet = doc.getObject(spreadsheet_name)
                height_value = spreadsheet.get(alias_name)
            except Exception as e:
                App.Console.PrintError(f"Fehler beim Abrufen des Werts: {e}")
                return

            # Teilen Sie den Wert durch 0,5 und berechnen Sie die Anzahl der Punkte
            num_points = 1

            # Abstand zwischen den Punkten
            spacing = Rohrabstand_value 

            # Initialer Y-Wert für den ersten Punkt
            initial_y = Rohrabstand_value * 0.5

            # Berechnen Sie die Punkte
            points = draw_points(num_points, spacing, initial_y)

            # Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
            add_AdditivePipe(points, original_body)

            # Kopieren und verschieben Sie das Skript 4 Mal in X-Richtung
            for i in range(1, Rohr_breite_value):
                x_offset =  Rohrabstand_value * i
                add_AdditivePipe(points, original_body, x_offset)

            App.Console.PrintMessage(f"{num_points} Punkte wurden in Y-Richtung mit einem Abstand von {spacing} gezeichnet. Der erste Punkt hat den Y-Wert 17,5.")
            App.Console.PrintMessage(f"Das Skript wurde 4 Mal in X-Richtung verschoben, jeweils um 40 Einheiten.")

    else:
        App.Console.PrintMessage("Bedingungen nicht erfüllt. Das Skript wird nicht ausgeführt.\n")

if __name__ == "__main__":
    main()

import FreeCAD as App 

doc = App.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)

Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Unten_rechts_H_cell = spreadsheet.Unten_rechts_H
Unten_rechts_H_value = str(Unten_rechts_H_cell)

Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_V_value == "X" and Rohr_hoehe_value == 2:

 # Funktion zum Hinzufügen des kopierten Objekts an den berechneten Positionen
 def add_copied_objects(original_object, num_copies):
    copies = []
    for i in range(num_copies):
        copy = original_object.Shape.copy()
        x_offset = Rohrabstand_value * 1.5  + i * Rohrabstand_value * 2
        z_offset = Rohrlaenge_value
        copy.Placement.Base.x = x_offset
        copy.Placement.Base.z = z_offset
        copies.append(copy)
    return copies

 # Funktion zum Hinzufügen des kopierten Objekts an den berechneten Positionen
 def add_copied_objects_2(original_object, num_copies):
    copies = []
    for i in range(num_copies):
        copy = original_object.Shape.copy()
        x_offset = (Rohrabstand_value / 2) + i * Rohrabstand_value * 2
        z_offset = Rohrlaenge_value
        y_offset = Rohr_hoehe_value * Rohrabstand_value - Rohrabstand_value  # Setzen Sie den Y-Wert auf 35
        copy.Placement.Base.x = x_offset
        copy.Placement.Base.z = z_offset
        copy.Placement.Base.y = y_offset
        copies.append(copy)
    return copies

 # Hauptskript
 def main():
    # Annahme: Der Alias-Name ist bereits in einer Variable gespeichert
    Lamelle1x = "AdditivePipe001"

    # Holen Sie das vorhandene Objekt anhand des Alias-Namens
    original_object = App.ActiveDocument.getObject(Lamelle1x)

    # Überprüfen, ob das Objekt existiert
    if original_object:
        # Berechnen Sie die Anzahl der Kopien
        num_copies = (Rohr_breite_value - 1) // 2

        # Hinzufügen der kopierten Objekte an den berechneten Positionen
        copied_objects = add_copied_objects(original_object, num_copies)

        # Hinzufügen der kopierten Objekte zum Dokument
        for i, copy in enumerate(copied_objects, start=1):
            App.ActiveDocument.addObject("Part::Feature", f"Bogen_vorne_Copy_{i}").Shape = copy

        App.Console.PrintMessage(f"{num_copies} Kopien wurden erstellt und positioniert.")
    else:
        App.Console.PrintError("Das Objekt mit dem angegebenen Alias-Namen existiert nicht.")

    if original_object:
        # Berechnen Sie die Anzahl der Kopien
        num_copies =  int(Rohr_breite_value / 2)

        # Hinzufügen der kopierten Objekte an den berechneten Positionen
        copied_objects = add_copied_objects_2(original_object, num_copies)

        # Hinzufügen der kopierten Objekte zum Dokument
        for j, copy in enumerate(copied_objects, start=1):
            App.ActiveDocument.addObject("Part::Feature", f"Bogen_vorne_Copy_{j}").Shape = copy

        App.Console.PrintMessage(f"{num_copies} Kopien wurden erstellt und positioniert.")
    else:
        App.Console.PrintError("Das Objekt mit dem angegebenen Alias-Namen existiert nicht.")
if __name__ == "__main__":
    main()
else:
        App.Console.PrintMessage("Bedingungen nicht erfüllt. Das Skript wird nicht ausgeführt.\n")
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_links_V_cell = spreadsheet.Oben_links_V
Oben_links_V_value = str(Oben_links_V_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point + App.Vector(x_offset + initial_x, y_offset, z_offset)
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value == 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_unten_hin_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_unten_hin_horizontal').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    for i in range(int(Rohr_breite_value / 2 )):
        Bogen_weg_vertikal = "AdditivePipe"
        original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = 2
        spacing_1 = Rohrabstand_value 
        initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * 2 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        z_offset = 0  # Passen Sie diesen Wert nach Bedarf an
        initial_x = Rohrabstand_value * 0.5
        add_AdditivePipe(points_1, original_body_weg_1, x_offset, z_offset,initial_x)
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value == 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_vertikal= "AdditivePipe001"
    original_body_weg_2 = App.ActiveDocument.getObject(Bogen_weg_vertikal)
    Num_points_1 = 1
    spacing_1 = Rohrabstand_value 
    initial_y = Rohrabstand_value / 2  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = (Rohr_breite_value - 1) * Rohrabstand_value
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    initial_x = 0
    # Hier wird z_offset separat für den z-Wert berücksichtigt
    add_AdditivePipe(points_1, original_body_weg_2, x_offset, 0, initial_x, z_offset)
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value == 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_horizontal = "AdditivePipe002"
    original_body_weg_2 = App.ActiveDocument.getObject(Bogen_weg_horizontal)
    range_wert = int(Rohr_breite_value / 2 - 1)
    for i in range(range_wert):
        Num_points_1 = 2
        spacing_1 = Rohrabstand_value 
        initial_y = 0    # Setzen Sie den Anfangswert für die Y-Position
        points_2 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * 2 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        z_offset = 1000   # Passen Sie diesen Wert nach Bedarf an
        initial_x = Rohrabstand_value * 1.5
        add_AdditivePipe(points_2, original_body_weg_2, x_offset, 0, initial_x, z_offset)
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_V_value == "X" and Rohr_hoehe_value == 2:
    FreeCAD.ActiveDocument.removeObject("AdditivePipe")
    FreeCAD.ActiveDocument.removeObject("AdditivePipe001")
    FreeCAD.ActiveDocument.removeObject("AdditivePipe002")
###############################################################
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = (Rohr_hoehe_value - 1) * Rohrabstand_value
    initial_x = Rohrabstand_value / 2 
    x_offset = Rohrabstand_value * 2 
    num_copies = Rohr_breite_value / 2 
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    
    # Hier können Sie den horizontalen Abstand zwischen den Objekten festlegen
    x_between_objects = Rohrabstand_value * 2   # Beispielwert, ändern Sie dies entsprechend Ihrer Anforderungen
    
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x + i * x_between_objects, initial_y, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
 

def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
    App.ActiveDocument.recompute()



   
    App.ActiveDocument.recompute()
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = 0
    initial_x = Rohrabstand_value * 1.5 
    x_offset = Rohrabstand_value * 2
    num_copies = Rohr_breite_value / 2 - 1
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    
    # Hier konnen Sie den horizontalen Abstand zwischen den Objekten festlegen
    x_between_objects = Rohrabstand_value * 2 # Beispielwert, ändern Sie dies entsprechend Ihrer Anforderungen
    
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x + i * x_between_objects, initial_y, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
    
    App.ActiveDocument.recompute()
#Nicht vergessen if command beenden #Nicht vergessen if command beenden #Nicht vergessen if command beenden #Nicht vergessen if command beenden 
import FreeCAD as App
import Part

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_vertikal = "AdditivePipe001"
    original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
    Num_points_1 = (Rohr_hoehe_value - 1) * 0.5
    spacing_1 = Rohrabstand_value * 2
    initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg, x_offset, z_offset)
    for i in range(Rohr_breite_value):
        Bogen_weg_vertikal = "AdditivePipe001"
        original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = (Rohr_hoehe_value - 1) * 0.5
        spacing_1 = Rohrabstand_value * 2
        initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = 35 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        add_AdditivePipe(points_1, original_body_weg, x_offset, z_offset)
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)

def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
    App.ActiveDocument.recompute()

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_H_value == "X" and Rohr_hoehe_value > 2:
  FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_hin.FCStd")
  App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_hin').getObject('AdditivePipe'), True)
  anderes_bogen_dokument_name = "Unnamed"
  FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
  Bogen_vertikal_hin = "AdditivePipe002"
  original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
  Num_points_1 = Rohr_hoehe_value / 2
  spacing_1 = Rohrabstand_value * 2
  initial_y = 0.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
  points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
  x_offset = 0 # Passen Sie diesen Wert nach Bedarf an
  add_AdditivePipe(points_1, original_body_weg, x_offset)
  for i in range(Rohr_breite_value):
   Bogen_weg_vertikal = "AdditivePipe002"
   original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
   Num_points_1 = Rohr_hoehe_value / 2
   spacing_1 = Rohrabstand_value * 2
   initial_y = Rohrabstand_value / 2  # Hier setzen Sie den Anfangswert für die Y-Position
   points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
   x_offset = Rohrabstand_value * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
   add_AdditivePipe(points_1, original_body_weg, x_offset)
#Wichtig für Springer etc.
import FreeCAD

# Funktion zum Finden und Löschen des gewünschten Objekts
def find_and_delete_bogen_object():
    # Holen des aktiven Dokuments
    doc = FreeCAD.ActiveDocument
    
    # Liste aller Objekte im Dokument
    objects = doc.Objects
    
    # Variablen für das Objekt mit den gewünschten Eigenschaften
    target_object = None
    min_y_value = float('inf')
    max_x_value = float('-inf')
    
    # Durchlaufen aller Objekte im Dokument
    for obj in objects:
        # Überprüfen, ob der Objektname mit "Bogen" beginnt und Z-Wert = Rohrlaenge_value ist
        if obj.Name.startswith("Bogen") and obj.Placement.Base.z == Rohrlaenge_value:
            # Überprüfen der X- und Y-Werte der Position
            x_value = obj.Placement.Base.x
            y_value = obj.Placement.Base.y
            
            # Suchen nach dem höchsten X-Wert und dem niedrigsten Y-Wert
            if x_value > max_x_value or (x_value == max_x_value and y_value < min_y_value):
                max_x_value = x_value
                min_y_value = y_value
                target_object = obj
    
    # Objekt löschen, wenn es gefunden wurde
    if target_object:
        print(f"Das gefundene und gelöschte Objekt ist: {target_object.Name}")
        print(f"Position: X = {target_object.Placement.Base.x}, Y = {target_object.Placement.Base.y}, Z = {target_object.Placement.Base.z}")
        doc.removeObject(target_object.Name)
    else:
        print("Kein passendes Objekt gefunden.")

# Funktion aufrufen
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_H_value == "X" and Rohr_hoehe_value > 2:
 find_and_delete_bogen_object()
#Hinten#Hinten#Hinten#Hinten#Hinten#Hinten#Hinten#Hinten#Hinten#Hinten#Hinten#Hinten
def find_and_delete_bogen_object():
    # Holen des aktiven Dokuments
    doc = FreeCAD.ActiveDocument
    
    # Liste aller Objekte im Dokument
    objects = doc.Objects
    
    # Variablen für das Objekt mit den gewünschten Eigenschaften
    target_object = None
    min_y_value = float('inf')
    max_x_value = float('-inf')
    
    # Durchlaufen aller Objekte im Dokument
    for obj in objects:
        # Überprüfen, ob der Objektname mit "Bogen" beginnt und Z-Wert = Rohrlaenge_value ist
        if obj.Name.startswith("Bogen") and obj.Placement.Base.z == 0:
            # Überprüfen der X- und Y-Werte der Position
            x_value = obj.Placement.Base.x
            y_value = obj.Placement.Base.y
            
            # Suchen nach dem höchsten X-Wert und dem niedrigsten Y-Wert
            if x_value > max_x_value or (x_value == max_x_value and y_value < min_y_value):
                max_x_value = x_value
                min_y_value = y_value
                target_object = obj
    
    # Objekt löschen, wenn es gefunden wurde
    if target_object:
        print(f"Das gefundene und gelöschte Objekt ist: {target_object.Name}")
        print(f"Position: X = {target_object.Placement.Base.x}, Y = {target_object.Placement.Base.y}, Z = {target_object.Placement.Base.z}")
        doc.removeObject(target_object.Name)
    else:
        print("Kein passendes Objekt gefunden.")
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_H_value == "X" and Rohr_hoehe_value > 2:
 find_and_delete_bogen_object()
def add_AdditivePipe(points, original_body, x_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
    App.ActiveDocument.recompute()
# Beispiel für die Verwendung der Funktion mit einem spezifischen Rohrlänge-Wert
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Unten_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg_springer.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg_springer').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_vertikal = "AdditivePipe003"
    original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
    Num_points_1 = 1
    spacing_1 = 0
    initial_y = Rohrabstand_value * 2 # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset =  10  + (Rohr_breite_value - 1) * Rohrabstand_value
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg, x_offset, z_offset)
###########################################
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    import FreeCAD
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_hin.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_hin').getObject('AdditivePipe'), True)
    anderes_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_dokument_name)
    import FreeCAD
    # Gui.runCommand('Std_DlgMacroRecord',0)
    ### Begin command Std_Open
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_unten_hin_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_unten_hin_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_hin_vertikal = "AdditivePipe"
    original_body = App.ActiveDocument.getObject(Bogen_hin_vertikal)

#SCHLEIFE DER MASSEN
    # Überprüfen, ob der Körper existiert
    if original_body:
        # Ihr Spreadsheet und der Alias-Name
        spreadsheet_name = "Spreadsheet"
        alias_name = "Rohr_hoehe"

        # Holen Sie den Wert aus dem Spreadsheet
        try:
            doc = App.activeDocument()
            spreadsheet = doc.getObject(spreadsheet_name)
            height_value = spreadsheet.get(alias_name)
        except Exception as e:
            App.Console.PrintError(f"Fehler beim Abrufen des Werts: {e}")

        # Teilen Sie den Wert durch 0,5 und berechnen Sie die Anzahl der Punkte
        num_points = Rohr_hoehe_value / 2

        # Abstand zwischen den Punkten
        spacing = Rohrabstand_value * 2

        # Initialer Y-Wert für den ersten Punkt
        initial_y = Rohrabstand_value / 2

        # Berechnen Sie die Punkte
        points = draw_points(num_points, spacing, initial_y)

        # Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
        add_AdditivePipe(points, original_body)
#SCHLEIFE DER MASSEN
        # Kopieren und verschieben Sie das Skript 4 Mal in X-Richtung
        for i in range(1, Rohr_breite_value - 2):
            x_offset = Rohrabstand_value * i
            add_AdditivePipe(points, original_body, x_offset)

        App.Console.PrintMessage(f"{num_points} Punkte wurden in Y-Richtung mit einem Abstand von {spacing} gezeichnet. Der erste Punkt hat den Y-Wert 17,5.")
        App.Console.PrintMessage(f"Das Skript wurde 4 Mal in X-Richtung verschoben, jeweils um 40 Einheiten.")
    else:
        print("Nein")
else:
    print("unter 2 oder 2")
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    Bogen_hin_horizontal = "AdditivePipe001"
    original_body_1 = App.ActiveDocument.getObject(Bogen_hin_horizontal)
    Num_points_1 = Rohr_hoehe_value
    spacing_1 = Rohrabstand_value
    initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = (Rohr_breite_value-1)* Rohrabstand_value - (Rohrabstand_value/2)  # Setzen Sie den x_offset-Wert entsprechend Ihren Anforderungen
    add_AdditivePipe(points_1, original_body_1, x_offset)

#Rückseite erfolreich


def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_vertikal= "AdditivePipe002"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_vertikal)
    Num_points_1 =(Rohr_hoehe_value - 1) * 0.5
    spacing_1 = Rohrabstand_value * 2
    initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1,original_body_weg_1, x_offset, z_offset)
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_weg_vertikal= "AdditivePipe002"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_vertikal)
    Num_points_1 = 1
    spacing_1 = 1
    initial_y = (Rohr_hoehe_value - 1.5) * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 1 + (Rohr_breite_value - 1) * Rohrabstand_value
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1,original_body_weg_1, x_offset, z_offset)
    for i in range(Rohr_breite_value - 2):
        Bogen_weg_vertikal = "AdditivePipe002"
        original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = (Rohr_hoehe_value - 1) * 0.5
        spacing_1 = Rohrabstand_value * 2
        initial_y = 1.5 * Rohrabstand_value  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
        add_AdditivePipe(points_1, original_body_weg_1, x_offset, z_offset)
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_x):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_x, y_value):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(x_value, y_value, 0))  
    return points

def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, y_offset, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_weg_horizontal= "AdditivePipe003"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_horizontal)
    Num_points_1 = (Rohr_breite_value - 2) / 2 
    spacing_1 = Rohrabstand_value * 2
    initial_x = Rohrabstand_value /  2   # Hier setzen Sie den Anfangswert für die Y-Position
    y_value = (Rohr_hoehe_value - 1) * Rohrabstand_value # Setzen Sie hier den gewünschten y-Wert ein
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
    x_offset = 0
    y_offset = 0  # Set the desired y offset here
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg_1, x_offset, y_offset, z_offset)

    draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_weg_horizontal= "AdditivePipe003"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_weg_horizontal)
    Num_points_1 = (Rohr_breite_value - 2) / 2 
    spacing_1 = Rohrabstand_value * 2
    initial_x = Rohrabstand_value * 1.5   # Hier setzen Sie den Anfangswert für die Y-Position
    y_value = 0 # Setzen Sie hier den gewünschten y-Wert ein
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
    x_offset = 0
    y_offset = 0  # Set the desired y offset here
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg_1, x_offset, y_offset, z_offset)

    draw_points_1(Num_points_1, spacing_1, initial_x, y_value)
import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_x):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_x, y_value):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(x_value, y_value, 0))  
    return points
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, y_offset, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
def add_AdditivePipe_1(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


import FreeCAD

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_unten_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_unten_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe002"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = Rohrabstand_value * 1.5
    initial_x = (Rohr_breite_value - 2) * Rohrabstand_value
    y_offset = Rohrabstand_value * 2 
    num_copies = (Rohr_hoehe_value - 2) / 2
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x, initial_y + i * y_offset, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
    App.ActiveDocument.recompute()

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
    anderes_memo_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_memo_dokument_name)
    Bogen_unten_weg_horizontal = "AdditivePipe002"
    original_body_weg_1 = App.ActiveDocument.getObject(Bogen_unten_weg_horizontal)
    initial_y = Rohrabstand_value / 2 
    initial_x = (Rohr_breite_value - 1) * Rohrabstand_value
    y_offset = Rohrabstand_value * 2
    num_copies = (Rohr_hoehe_value - 2) / 2
    z_offset = Rohrlaenge_value  # Beispielwert für den Z-Offset, bitte anpassen
    for i in range(int(num_copies)):
        copy = original_body_weg_1.Shape.copy()
        new_position = FreeCAD.Vector(initial_x, initial_y + i * y_offset, z_offset)
        copy.Placement.Base = new_position
        App.ActiveDocument.addObject("Part::Feature", "Bogen" + str(i+1)).Shape = copy
        y_offset = Rohrabstand_value * 2 
    App.ActiveDocument.recompute()



import FreeCAD

# Funktion zum Finden und Löschen des gewünschten Objekts
def find_and_delete_bogen_object():
    # Holen des aktiven Dokuments
    doc = FreeCAD.ActiveDocument
    
    # Liste aller Objekte im Dokument
    objects = doc.Objects
    
    # Variablen für das Objekt mit den gewünschten Eigenschaften
    target_object = None
    max_y_value = float('-inf')
    max_x_value = float('-inf')
    
    # Durchlaufen aller Objekte im Dokument
    for obj in objects:
        # Überprüfen, ob der Objektname mit "Bogen" beginnt und Z-Wert = 0 ist
        if obj.Name.startswith("Bogen") and obj.Placement.Base.z == 0:
            # Überprüfen der X- und Y-Werte der Position
            x_value = obj.Placement.Base.x
            y_value = obj.Placement.Base.y
            
            # Suchen nach dem höchsten X- und Y-Wert
            if x_value > max_x_value or (x_value == max_x_value and y_value > max_y_value):
                max_x_value = x_value
                max_y_value = y_value
                target_object = obj
    
    # Objekt löschen, wenn es gefunden wurde
    if target_object:
        print(f"Das gefundene und gelöschte Objekt ist: {target_object.Name}")
        print(f"Position: X = {target_object.Placement.Base.x}, Y = {target_object.Placement.Base.y}, Z = {target_object.Placement.Base.z}")
        doc.removeObject(target_object.Name)
    else:
        print("Kein passendes Objekt gefunden.")

# Funktion aufrufen
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_rechts_H_value == "X" and Rohr_hoehe_value > 2:
 find_and_delete_bogen_object()


import FreeCAD

def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)
# Funktion zum Zeichnen der Punkte in FreeCAD
def draw_points(num_points, spacing, initial_x):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_x, initial_y):
    points = []
    for i in range(int(num_points)):
        x_value = initial_x + i * spacing
        points.append(FreeCAD.Vector(x_value, y_value, 0))  
    return points
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(FreeCAD.Vector(x_offset, y_offset, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy
def add_AdditivePipe_1(points, original_body, x_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(x_offset, 0, 0))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


import FreeCAD


# Dokument aktualisieren
App.ActiveDocument.recompute()
#########################################################################
def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False


def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point + App.Vector(x_offset + initial_x, y_offset, z_offset)
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point.add(App.Vector(x_offset + initial_x, y_offset, z_offset))
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

# Call the function with the corrected arguments
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_weg_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_weg_horizontal').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_vertikal_hin = "AdditivePipe"
    original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
    Num_points_1 = Rohr_hoehe_value 
    spacing_1 = Rohrabstand_value
    initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0   # Passen Sie diesen Wert nach Bedarf an
    z_offset = Rohrlaenge_value  # Passen Sie diesen Wert nach Bedarf an
    initial_x = Rohrabstand_value * 1.5   # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)
    Range_wert = int(Rohr_breite_value / 2 - 2)
    for i in range(Range_wert):
        Bogen_weg_vertikal = "AdditivePipe"
        initial_x = Rohrabstand_value * 3.5
        original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = Rohr_hoehe_value 
        spacing_1 = Rohrabstand_value 
        initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * 2 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)
import FreeCAD as App

doc = App.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_links_V_cell = spreadsheet.Oben_links_V
Oben_links_V_value = str(Oben_links_V_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)


def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False


def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point + App.Vector(x_offset + initial_x, y_offset, z_offset)
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy

if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_H_value == "X" and Rohr_hoehe_value > 2:
   FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_vertikal_weg.FCStd")
   App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_vertikal_weg').getObject('AdditivePipe'), True)
   anderes_bogen_dokument_name = "Unnamed"
   FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
   Bogen_vertikal_hin = "AdditivePipe001"
   original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
   num_points = int(Rohr_hoehe_value / 2 - 1)
   spacing = Rohrabstand_value * 2 
   initial_y = Rohrabstand_value * 1.5 
   initial_x = 0
   x_offset = 0
   z_offset = Rohrlaenge_value
   points = create_points(num_points, spacing, initial_y, initial_x)
   create_pipes(points, original_body_weg, x_offset, z_offset, initial_x)


if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_H_value == "X" and Rohr_hoehe_value > 2:
   num_points = int(Rohr_hoehe_value / 2)
   spacing = Rohrabstand_value * 2 
   initial_y = Rohrabstand_value / 2  
   initial_x = 0
   x_offset = int((Rohr_breite_value -1)* Rohrabstand_value)
   z_offset = Rohrlaenge_value
   points = create_points(num_points, spacing, initial_y, initial_x)
   create_pipes(points, original_body_weg, x_offset, z_offset, initial_x)
   


import FreeCAD as App

doc = App.ActiveDocument
spreadsheet = doc.Spreadsheet
Rohrlaenge_cell = spreadsheet.Rohrlaenge
Rohrlaenge_value = int(Rohrlaenge_cell)
Eingang_Rohrlaenge_cell = spreadsheet.Eingang_Rohrlaenge
Eingang_Rohrlaenge_value = int(Eingang_Rohrlaenge_cell)
Eingang_Rohrdurchmesser_cell = spreadsheet.Eingang_Rohrdurchmesser
Eingang_Rohrdurchmesser_value = int(Eingang_Rohrdurchmesser_cell)
Rohrabstand_cell = spreadsheet.Rohrabstand
Rohrabstand_value = int(Rohrabstand_cell)

Oben_links_H_cell = spreadsheet.Oben_links_H
Oben_links_H_value = str(Oben_links_H_cell)
Oben_links_V_cell = spreadsheet.Oben_links_V
Oben_links_V_value = str(Oben_links_V_cell)
Oben_rechts_V_cell = spreadsheet.Oben_rechts_V
Oben_rechts_V_value = str(Oben_rechts_V_cell)
Unten_links_V_cell = spreadsheet.Unten_links_V
Unten_links_V_value = str(Unten_links_V_cell)
Unten_rechts_V_cell = spreadsheet.Unten_rechts_V
Unten_rechts_V_value = str(Unten_rechts_V_cell)
Rohr_hoehe_cell = spreadsheet.Rohr_hoehe
Rohr_hoehe_value = int(Rohr_hoehe_cell)
Rohr_breite_cell = spreadsheet.Rohr_breite
Rohr_breite_value = int(Rohr_breite_cell)


def is_even(value):
    try:
        num = int(value)
        return num % 2 == 0
    except ValueError:
        return False


def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy


def draw_points(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points
def draw_points_1(num_points, spacing, initial_y):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(FreeCAD.Vector(0, y_value, 0))
    return points

# Funktion zum Hinzufügen des AdditivePipe-Objekts an den berechneten Punkten
def add_AdditivePipe(points, original_body, x_offset=0, y_offset=0, initial_x=0, z_offset=0):
    for point in points:
        copy = original_body.Shape.copy()
        # Adjust the Base position by adding the offsets
        new_base = point + App.Vector(x_offset + initial_x, y_offset, z_offset)
        copy.Placement.Base = new_base
        # Create a new object with the copied shape
        new_object = App.ActiveDocument.addObject("Part::Feature", "Bogen")
        new_object.Shape = copy
    # Recompute the document to update the changes
    App.ActiveDocument.recompute()

def create_points(num_points, spacing, initial_y, initial_x):
    points = []
    for i in range(int(num_points)):
        y_value = initial_y + i * spacing
        points.append(App.Vector(initial_x, y_value, 0))
    return points


def create_pipes(points, Original_body_weg, x_offset, z_offset, initial_x):
    for point in points:
        copy = Original_body_weg.Shape.copy()
        copy.Placement.Base = point.add(App.Vector(initial_x + x_offset, 0, z_offset))
        App.ActiveDocument.addObject("Part::Feature", "Bogen").Shape = copy

# Call the function with the corrected arguments
if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_H_value == "X" and Rohr_hoehe_value > 2:
    FreeCAD.openDocument(r"C:\Users\jamin\OneDrive\Desktop\Freecad Bücherei\Bogen_unten_hin_horizontal.FCStd")
    App.getDocument('Unnamed').moveObject(App.getDocument('Bogen_unten_hin_horizontal').getObject('AdditivePipe'), True)
    anderes_bogen_dokument_name = "Unnamed"
    FreeCAD.setActiveDocument(anderes_bogen_dokument_name)
    Bogen_vertikal_hin = "AdditivePipe002"
    original_body_weg = App.ActiveDocument.getObject(Bogen_vertikal_hin)
    Num_points_1 = Rohr_hoehe_value 
    spacing_1 = Rohrabstand_value
    initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
    points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
    x_offset = 0   # Passen Sie diesen Wert nach Bedarf an
    z_offset = 0  # Passen Sie diesen Wert nach Bedarf an
    initial_x = Rohrabstand_value * 0.5  # Passen Sie diesen Wert nach Bedarf an
    add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)
    Range_wert = int(Rohr_breite_value / 2 - 1)
    for i in range(Range_wert):
        Bogen_weg_vertikal = "AdditivePipe002"
        initial_x = Rohrabstand_value * 2.5
        original_body_weg = App.ActiveDocument.getObject(Bogen_weg_vertikal)
        Num_points_1 = Rohr_hoehe_value 
        spacing_1 = Rohrabstand_value 
        initial_y = 0  # Hier setzen Sie den Anfangswert für die Y-Position
        points_1 = draw_points_1(Num_points_1, spacing_1, initial_y)
        x_offset = Rohrabstand_value * 2 * i  # Anpassen des X-Offsets entsprechend Ihrem Bedarf
        add_AdditivePipe(points_1, original_body_weg, x_offset=x_offset, z_offset=z_offset, initial_x=initial_x)


if is_even(Rohr_breite_value) and is_even(Rohr_hoehe_value) and Unten_links_V_value == "X" and Oben_links_H_value == "X" and Rohr_hoehe_value > 2:
 FreeCAD.ActiveDocument.removeObject("AdditivePipe")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe001")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe002")
 FreeCAD.ActiveDocument.removeObject("AdditivePipe004")
anderes_dokument_name = "Unnamed"

# Überprüfen, ob das Dokument existiert
if FreeCAD.getDocument(anderes_dokument_name):
    # Setze das andere Dokument als aktives Dokument
    FreeCAD.setActiveDocument(anderes_dokument_name)
    # Aktualisiere die Ansicht
    FreeCAD.ActiveDocument.recompute()
def find_and_delete_specific_bogen_in_unnamed():
    # Holen des Dokuments mit dem Namen "Unnamed"
    doc = FreeCAD.getDocument("Unnamed")
    
    # Überprüfen, ob das Dokument existiert
    if not doc:
        print("Dokument 'Unnamed' wurde nicht gefunden.")
        return
    
    # Liste aller Objekte im Dokument
    objects = doc.Objects
    
    # Variablen für das Zielobjekt
    target_object = None
    min_x_value = float('inf')
    max_y_value = float('-inf')
    
    # Durchlaufen aller Objekte im Dokument
    for obj in objects:
        # Überprüfen, ob der Objektname mit "Bogen" beginnt und der Z-Wert 0 ist
        if obj.Name.startswith("Bogen") and obj.Placement.Base.z == 0:
            # Überprüfen der X- und Y-Werte der Position
            x_value = obj.Placement.Base.x
            y_value = obj.Placement.Base.y
            
            # Suchen nach dem Objekt mit dem niedrigsten X-Wert und höchsten Y-Wert
            if x_value < min_x_value or (x_value == min_x_value and y_value > max_y_value):
                min_x_value = x_value
                max_y_value = y_value
                target_object = obj
    
    # Objekt löschen, wenn es gefunden wurde
    if target_object:
        print(f"Das gefundene und zu löschende Objekt ist: {target_object.Name}")
        print(f"Position: X = {target_object.Placement.Base.x}, Y = {target_object.Placement.Base.y}, Z = {target_object.Placement.Base.z}")
        doc.removeObject(target_object.Name)
        # Dokument neu berechnen
        doc.recompute()
    else:
        print("Kein passendes Objekt gefunden.")

# Funktion aufrufen
find_and_delete_specific_bogen_in_unnamed()
print("HURENSOHNHURENSOHNHURENSOHN")

































########################################










##############################################################
# Annahme: Der Name des anderen Dokuments ist "MeinAnderesDokument"
anderes_dokument_name = "Unnamed"

# Überprüfen, ob das Dokument existiert 
if FreeCAD.getDocument(anderes_dokument_name):
    # Setze das andere Dokument als aktives Dokument
    FreeCAD.setActiveDocument(anderes_dokument_name)
    # Aktualisiere die Ansicht
    FreeCAD.ActiveDocument.recompute()
    print(f"{anderes_dokument_name} ist jetzt das aktive Dokument.")
else:
    print(f"Dokument mit dem Namen {anderes_dokument_name} nicht gefunden.")



FreeCAD.ActiveDocument.removeObject("AdditivePipe")
FreeCAD.ActiveDocument.removeObject("AdditivePipe001")
FreeCAD.ActiveDocument.removeObject("AdditivePipe003")
FreeCAD.ActiveDocument.removeObject("AdditivePipe004")
import FreeCAD

def delete_documents_except_unnamed():
    # Überprüfen, ob das Dokument aktiv ist
    if FreeCAD.ActiveDocument is None:
        print("Es gibt kein aktives Dokument.")
        return

    # Durchlaufen aller geöffneten Dokumente
    for document_name in FreeCAD.listDocuments():
        if document_name != "Unnamed":
            FreeCAD.closeDocument(document_name)
            print("Das Dokument '{}' wurde erfolgreich geloscht.".format(document_name))

# Aufruf der Funktion zum Löschen aller Dokumente außer "Unnamed"
delete_documents_except_unnamed()
import FreeCAD
anderes_memo_dokument_name = "Unnamed"
FreeCAD.setActiveDocument(anderes_memo_dokument_name)
def delete_all_planes():
    # Überprüfen, ob das Dokument aktiv ist
    if FreeCAD.ActiveDocument is None:
        print("Es gibt kein aktives Dokument.")
        return

    # Durchlaufen aller Objekte im aktiven Dokument
    for obj in FreeCAD.ActiveDocument.Objects:
        # Überprüfen, ob das Objekt ein Plane ist
        if obj.TypeId == 'PartDesign::Plane':
            # Objekt löschen
            FreeCAD.ActiveDocument.removeObject(obj.Name)
            print("Die Ebene '{}' wurde erfolgreich geloscht.".format(obj.Label))

# Aufruf der Funktion zum Löschen aller Ebenen im aktiven Dokument
delete_all_planes()
import FreeCAD as App

doc = FreeCAD.ActiveDocument
spreadsheet = doc.Spreadsheet
Beschichtung_cell = spreadsheet.Beschichtung
Beschichtung_value = str(Beschichtung_cell)

if Beschichtung_value == "None":
    # Funktion zum Färben von Körpern, deren Name mit bestimmten Präfixen beginnt, in Kupferfarbe
    def color_pipe_bodies(document):
        num_colored = 0
        prefixes = ["Pipe", "AdditivePipe", "Rohr", "Bogen"]
        for obj in document.Objects:
            try:
                # Überprüfen, ob das Objekt ein Körper ist und der Name mit einem der Präfixe beginnt
                if obj.isDerivedFrom("Part::Feature") and any(obj.Name.startswith(prefix) for prefix in prefixes):
                    # Überprüfen, ob das Objekt ein Volumenkörper ist
                    if obj.Shape.Volume > 0:
                        # Kupfermaterial zuweisen
                        obj.ViewObject.ShapeColor = (0.72, 0.45, 0.20)  # Kupferfarbe (RGB)
                        num_colored += 1
            except Exception as e:
                print("Fehler beim Färben des Körpers:", obj.Name, str(e))
        print("Anzahl der gefärbten Körper:", num_colored)

    # Aktives FreeCAD-Dokument erhalten
    doc = App.activeDocument()

    # Alle Körper im Dokument färben, deren Name mit bestimmten Präfixen beginnt, in Kupferfarbe
    color_pipe_bodies(doc)

    # Ansicht aktualisieren
    App.ActiveDocument.recompute()

