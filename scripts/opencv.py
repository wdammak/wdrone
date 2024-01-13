import cv2
import numpy as np

# Charger une image (remplacez le chemin d'accès par le chemin de votre image)
image_path = 'chemin/vers/votre/image.jpg'
image = cv2.imread(image_path)

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un flou pour réduire le bruit
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Utiliser la détection de contours
edges = cv2.Canny(blurred_image, 50, 150)

# Afficher l'image originale et le résultat de la détection de contours
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

