import json
import random
import sqlite3
from datetime import datetime, timedate
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "urban_mobility.db"
SCHEMA_PATH = BASE_DIR / "database"/ "schema.sql"

ZONE_LOOKUP = [
    (1, "Manhattan", "East Harlem", "Yellow"),
    (2, "Manhattan", "Upper East Side", "Yellow"),
    (3, "Queens", "JFK Airport", "Airport"),
    (4, "Brooklyn", "Downtown Brooklyn", "Boro"),
    (5, "Brooklyn", "Williamsburg", "Boro"),
    (6, "Queens", "Long Island City", "Boro"),
    (7, "Bronx", "Fordham", "Boro"),
    (8, "Staten Island", "St. George", "Boro"),
    (9, "Manhattan", "Chelsea", "Yellow"),
    (10, "Manhattan", "Midtown East", "Yellow"),
    (11, "Queens", "Astoria", "Boro"),
    (12, "Brooklyn", "Crown Heights", "Boro"),
    (13, "Queens", "Flushing", "Boro"),
    (14, "Bronx", "Mott Haven", "Boro"),
    (15, "Brooklyn", "Bedford-Stuyvesant", "Boro"),
    (16, "Manhattan", "Lower East Side", "Yellow"),
    (17, "Brooklyn", "Sunset Park", "Boro"),
    (18, "Queens", "Rockaway", "Boro"),
    (19, "Brooklyn", "Park Slope", "Boro"),
    (20, "Manhattan", "Financial District", "Yellow"),
    ]

