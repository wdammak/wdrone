from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connexion au véhicule
connection_string = '/dev/ttyUSB0'  # Remplacez par le port de votre véhicule
vehicle = connect(connection_string, baud=57600, wait_ready=True)

# Fonction pour armer et décoller le drone
def arm_and_takeoff(aTargetAltitude):
    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Fonction pour envoyer des données MAVLink personnalisées
def send_mavlink_data():
    # Exemple de données personnalisées
    custom_data = [1, 2, 3, 4]

    # Envoi des données MAVLink personnalisées
    vehicle.message_factory.command_long_send(
        0, 0,                       # target_system, target_component
        mavutil.mavlink.MAV_CMD_USER1, # command
        0,                           # confirmation
        *custom_data                 # param1, param2, param3, param4, param5, param6, param7
    )

# Décollage vers une altitude de 10 mètres
target_altitude = 10
arm_and_takeoff(target_altitude)

# Envoi de données MAVLink personnalisées
send_mavlink_data()

# Attendre un certain temps avant de revenir en mode RTL (Return To Launch)
time.sleep(30)

# Revenir en mode RTL
print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

# Attendre que le véhicule atteigne le point de départ avant de terminer le script
while not vehicle.mode.name == 'STABILIZE':
    print(" Waiting to reach home...")
    time.sleep(1)

# Fermer la connexion au véhicule
vehicle.close()

