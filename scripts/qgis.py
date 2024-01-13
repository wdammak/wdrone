from qgis.core import QgsApplication, QgsVectorLayer, QgsProject
from qgis.gui import QgsMapCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow

# Initialiser l'application QGIS
qgs = QgsApplication([], False)
qgs.initQgis()

# Créer une couche vectorielle à partir d'un fichier Shapefile (remplacez le chemin d'accès)
shp_path = 'chemin/vers/votre/fichier.shp'
layer = QgsVectorLayer(shp_path, 'Nom de la couche', 'ogr')

# Ajouter la couche au projet QGIS
QgsProject.instance().addMapLayer(layer)

# Afficher l'étendue de la couche sur une carte
canvas = QgsMapCanvas()
canvas.setExtent(layer.extent())
canvas.setLayers([layer])
canvas.show()

# Lancer l'application QGIS
app = QApplication([])
window = QMainWindow()
window.setCentralWidget(canvas)
window.show()
app.exec_()

