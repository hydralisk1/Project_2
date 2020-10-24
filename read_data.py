from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db_engine import eng

def get_planet_data():
    engine = create_engine(eng)
    Base = automap_base()
    Base.prepare(engine, reflect = True)

    Planets = Base.classes.planets
    Stars = Base.classes.stars
    Exo = Base.classes.exoplanets

    session = Session(engine)

    p_query = session.query(Planets.name, Planets.host_star, Planets.radius_e, Planets.temp_f, Planets.habit_code, Planets.circumference_k)
    s_query = session.query(Stars.star, Stars.temp_k, Stars.radius_s, Stars.gravity, Stars.gal_lat, Stars.gal_long, Stars.distance)
    e_query = session.query(Exo.exoPlanetName, Exo.PlanetMassEst, Exo.PlanetRadiusEst, Exo.PlanetTempType, Exo.PlanetDetection, Exo.DiscoverYr, Exo.StarConst, Exo.PotHabitableOptimistic, Exo.PotHabitableConservative, Exo.LastUpdate, Exo.StarRtAsc, Exo.StarDistance)

    p_keys = ["name", "host_star", "radius_e", "temp_f", "habit_code", "circumference_k"]
    s_keys = ["star", "temp_k", "radius_s", "gravity", "gal_lat", "gal_long", "distance"]
    e_keys = ["exoPlanetName", "PlanetMassEst", "PlanetRadiusEst", "PlanetTempType", "PlanetDetection", "DiscoverYr", "StarConst", "PotHabitableOptimistic", "PotHabitableConservative", "LastUpdate", "StarRtAsc", "StarDistance"]
    data = {
        "stars": [],
        "planets": [],
        "exoplanets": []
    }

    for row in p_query:
        temp_dict = {}
        for (key, i) in zip(p_keys, range(len(row))):
            temp_dict[key] = row[i]    
            data["planets"].append(temp_dict)

    for row in s_query:
        temp_dict = {}
        for (key, i) in zip(s_keys, range(len(row))):
            temp_dict[key] = row[i]    
            data["stars"].append(temp_dict)

    for row in e_query:
        temp_dict = {}
        for (key, i) in zip(e_keys, range(len(row))):
            temp_dict[key] = row[i]    
            data["exoplanets"].append(temp_dict)

    return data