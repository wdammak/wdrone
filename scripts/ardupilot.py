# wdrone/scripts/ardupilot_script.py

from dronekit import connect, VehicleMode
import time
import threading

# Connexion au simulateur SITL (remplacez le port si nécessaire)
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

class EventManager:
    def __init__(self):
        self.events = {}
        self.lock = threading.Lock()

    def add_event(self, event_name):
        with self.lock:
            self.events[event_name] = threading.Event()

    def set_event(self, event_name):
        with self.lock:
            if event_name in self.events:
                self.events[event_name].set()

    def wait_for_event(self, event_name, timeout=None):
        with self.lock:
            if event_name in self.events:
                return self.events[event_name].wait(timeout)
        return False

def move_to_location(latitude, longitude, altitude):
    # Fonction pour déplacer le drone vers une nouvelle position
    target_location = (latitude, longitude, altitude)
    vehicle.simple_goto(target_location)
    while True:
        # Attendre que le drone atteigne la destination
        current_location = vehicle.location.global_frame
        distance = current_location.distance_to(target_location)
        if distance < 1:
            break
        time.sleep(1)

def take_samples(parcelle_id):
    # Simulation de la prise d'analyses
    print(f"Drone prend des analyses de la parcelle {parcelle_id}...")
    # Code pour prendre des échantillons

def send_to_server(parcelle_id):
    # Simulation de l'envoi des analyses au serveur
    print(f"Analyses de la parcelle {parcelle_id} envoyées au serveur en temps réel.")

# Liste des parcelles à visiter chaque jour (exemple)
parcelles_a_visiter = [(37.7749, -122.4194, 10, "ParcelleA"), (37.7749, -122.4195, 10, "ParcelleB")]

# Création d'un gestionnaire d'événements
event_manager = EventManager()

def mission_thread():
    for parcelle in parcelles_a_visiter:
        move_to_location(*parcelle[:3])
        take_samples(parcelle[3])
        send_to_server(parcelle[3])
        event_manager.set_event(f"Parcelle_{parcelle[3]}_Terminee")
        # Attendre des instructions supplémentaires avant de passer à la parcelle suivante
        event_manager.wait_for_event(f"Instructions_{parcelle[3]}", timeout=None)

# Création d'un fil d'exécution pour la mission
mission_thread = threading.Thread(target=mission_thread)

# Exécution de la mission
mission_thread.start()

# Simulation d'instructions supplémentaires pour la première parcelle
time.sleep(5)
event_manager.set_event("Instructions_ParcelleA")

# Attente de la fin de la mission
mission_thread.join()

# Atterrissage et fermeture de la connexion
vehicle.mode = VehicleMode("LAND")
while not vehicle.location.global_relative_frame.alt == 0:
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    time.sleep(1)
vehicle.close()
print("Connexion au drone fermée.")
