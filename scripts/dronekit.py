from dronekit import connect, VehicleMode
import time

# Connexion au simulateur SITL (remplacez le port si nécessaire)
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

# Affichage des informations sur le véhicule
print("Connected to vehicle on: %s" % vehicle.connection_string)
print("Mode: %s" % vehicle.mode.name)
print("GPS: %s" % vehicle.gps_0)

# Changement du mode du véhicule à GUIDED
vehicle.mode = VehicleMode("GUIDED")

# Attendre que le véhicule atteigne le mode GUIDED
while not vehicle.mode.name == 'GUIDED':
    print(" Waiting for GUIDED mode...")
    time.sleep(1)

# Décollage à une altitude de 10 mètres
print("Taking off to 10 meters...")
vehicle.simple_takeoff(10)

# Attendre que le véhicule atteigne l'altitude cible
while vehicle.location.global_relative_frame.alt < 10:
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    time.sleep(1)

# Atterrissage
print("Landing...")
vehicle.mode = VehicleMode("LAND")

# Attendre que le véhicule atteigne le sol avant de terminer
while not vehicle.location.global_relative_frame.alt == 0:
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    time.sleep(1)

# Fermer la connexion au véhicule
vehicle.close()

