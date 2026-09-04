from fastapi import FastAPI

from app.engines.flood_engine import simulate_flood
from app.engines.risk_engine import calculate_all_risks
from app.engines.route_engine import (
    find_safest_route,
    calculate_all_routes
)
from app.engines.shelter_engine import allocate_people_to_shelters
from app.engines.rescue_engine import allocate_rescue_teams
from app.engines.whatif_engine import simulate_what_if
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="ResQTwin API",
    description="AI-Powered Disaster Management Digital Twin",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to ResQTwin API",
        "status": "running"
    }


@app.get("/api/flood/simulate")
def flood_simulation(water_level: float = 4):
    return simulate_flood(water_level)


@app.get("/api/risk/assess")
def risk_assessment(water_level: float = 4):
    return calculate_all_risks(water_level)


@app.get("/api/routes/all")
def all_evacuation_routes(water_level: float = 4):
    return calculate_all_routes(water_level)


@app.get("/api/routes/find")
def evacuation_route(
    building_id: str,
    water_level: float = 4
):
    return find_safest_route(
        building_id,
        water_level
    )
@app.get("/api/shelters/allocate")
def shelter_allocation(water_level: float = 4):
    return allocate_people_to_shelters(water_level)

@app.get("/api/rescue/allocate")
def rescue_allocation(water_level: float = 4):
    return allocate_rescue_teams(water_level)

@app.get("/api/what-if/flood")
def what_if_flood(
    current_water_level: float = 4,
    simulated_water_level: float = 6
):
    return simulate_what_if(
        current_water_level,
        simulated_water_level
    )