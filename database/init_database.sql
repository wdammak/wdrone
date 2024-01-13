-- Initialisation de la base de données avec les tables nécessaires

-- Table des tâches
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status TEXT
);

-- Table des drones
CREATE TABLE IF NOT EXISTS drones (
    id INTEGER PRIMARY KEY,
    drone_name TEXT NOT NULL,
    serial_number TEXT UNIQUE NOT NULL,
    status TEXT
);

-- Table des parcelles
CREATE TABLE IF NOT EXISTS parcelles (
    id INTEGER PRIMARY KEY,
    parcelle_name TEXT NOT NULL,
    location_lat REAL,
    location_lon REAL,
    area REAL
);

-- Table des capteurs
CREATE TABLE IF NOT EXISTS capteurs (
    id INTEGER PRIMARY KEY,
    sensor_name TEXT NOT NULL,
    type TEXT,
    status TEXT
);

-- Table des données des capteurs
CREATE TABLE IF NOT EXISTS donnees_capteurs (
    id INTEGER PRIMARY KEY,
    sensor_id INTEGER,
    drone_id INTEGER,
    parcelle_id INTEGER,
    value REAL,
    timestamp TIMESTAMP,
    FOREIGN KEY(sensor_id) REFERENCES capteurs(id),
    FOREIGN KEY(drone_id) REFERENCES drones(id),
    FOREIGN KEY(parcelle_id) REFERENCES parcelles(id)
);

-- Table des utilisateurs
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

-- Table des missions
CREATE TABLE IF NOT EXISTS missions (
    id INTEGER PRIMARY KEY,
    drone_id INTEGER,
    task_id INTEGER,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status TEXT,
    FOREIGN KEY(drone_id) REFERENCES drones(id),
    FOREIGN KEY(task_id) REFERENCES tasks(id)
);

-- Table des notifications
CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY,
    message TEXT NOT NULL,
    timestamp TIMESTAMP
);

-- Table des configurations
CREATE TABLE IF NOT EXISTS configurations (
    id INTEGER PRIMARY KEY,
    key TEXT NOT NULL,
    value TEXT NOT NULL
);

-- Table des rapports
CREATE TABLE IF NOT EXISTS rapports (
    id INTEGER PRIMARY KEY,
    mission_id INTEGER,
    content TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY(mission_id) REFERENCES missions(id)
);

