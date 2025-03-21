from datetime import datetime
from flask import abort
from flask import abort, make_response



def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    return list(PEOPLE.values())

def create(person):
    name = person.get("name")

    if name not in PEOPLE:
        PEOPLE[name] = {
            "name": name,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[name], 201
    else:
        abort(
            406,
            f"Person with name {name} already exists",
        )

def read_one(name):
    if name in PEOPLE:
        return PEOPLE[name]
    else:
        abort(
            404, f"Person with name {name} not found"
        )


def update(name, person):
    if name in PEOPLE:
        PEOPLE[name]["name"] = person.get("name", PEOPLE[name]["name"]) 
        PEOPLE[name]["email"] = person.get("email", PEOPLE[name]["email"])
        PEOPLE[name]["fav_frame"] = person.get("fav_frame", PEOPLE[name]["fav_frame"])
        PEOPLE[name]["timestamp"] = get_timestamp()
        return PEOPLE[name]
    else:
        abort(404, f"Person with name {name} not found")


def delete(name):
    if name in PEOPLE:
        del PEOPLE[name]
        return make_response(
            f"{name} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with {name} not found"
        )


PEOPLE = {
    "New_Player": {
        "name": "New_player",
        "email": "heyitsmyemail@gmail.com",
        "fav_frame": "Excalibur",
        "timestamp": get_timestamp(),
    },
    "Gary": {
        "name": "Gary",
        "email": "yoitsgary@gmail.com",
        "fav_frame": "Atlas",
        "timestamp": get_timestamp(),
    },
    "OrangeJuice": {
        "name": "OrangeJuice",
        "email": "daniel@hotmail.com",
        "fav_frame": "Gaus",
        "timestamp": get_timestamp(),
    }
}

