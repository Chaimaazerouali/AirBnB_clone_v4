#!/usr/bin/python3
'''Contains the amenities view for the API.'''
from flask import jsonify, request
from werkzeug.exceptions import NotFound, MethodNotAllowed, BadRequest

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity

@app_views.route("/amenities", methods=["GET"], strict_slashes=False)
def amenity_get():
    """
    retrieves all Amenity objects
    """
    a_list = []
    all_obj = storage.all("Amenity")
    for obj in all_obj.values():
        a_list.append(obj.to_json())

    return jsonify(a_list)


@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def amenity_add():
    """
    add amenity route
    """
    all_json = request.get_json(silent=True)
    if all_json is None:
        abort(400, 'Not a JSON')
    if "name" not in am_json:
        abort(400, 'Missing name')

    n_amty = Amenity(**all_json)
    n_amty.save()
    res = jsonify(n_amty.to_json())
    res.status_code = 201

    return resp


@app_views.route("/amenities/<amenity_id>",  methods=["GET"],
                 strict_slashes=False)
def amty_id(amenity_id):
    """
    gets a specific Amenity object by ID
    """

    fetch_obj = storage.get("Amenity", str(amenity_id))

    if fetch_obj is None:
        abort(404)

    return jsonify(fetch_obj.to_json())


@app_views.route("/amenities/<amenity_id>",  methods=["PUT"],
                 strict_slashes=False)
def amty_put(amenity_id):
    """
    updates Amenity object by ID
    """
    all_json = request.get_json(silent=True)
    if all_json is None:
        abort(400, 'Not a JSON')
    fetch_obj = storage.get("Amenity", str(amenity_id))
    if fetch_obj is None:
        abort(404)
    for key, val in all_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(fetch_obj, key, val)
    fetch_obj.save()
    return jsonify(fetch_obj.to_json())


@app_views.route("/amenities/<amenity_id>",  methods=["DELETE"],
                 strict_slashes=False)
def amenity_del(amenity_id):
    """
    remove Amenity by id
    """

    fetch_obj = storage.get("Amenity", str(amenity_id))

    if fetch_obj is None:
        abort(404)

    storage.delete(fetched_obj)
    storage.save()

    return jsonify({})
