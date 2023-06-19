from flask import Blueprint, Response
from application.api.mylocal.gig.Ent import Ent
from application.api.mylocal.gig.GIGTable import GIGTable
import json

bp = Blueprint('mylocal', __name__)
url_prefix = '/mylocal_service'

@bp.route('/')
def index():
    """Index."""
    data = 'mylocal_service Running.!'
    return data

@bp.route('/entity/<string:entity_id>')
def entity(entity_id):
    """Get entity by entity id."""
    print('/entity/ entity_id: ', entity_id)
    entity = Ent.from_id(entity_id)
    return Response(entity.to_json(), mimetype='application/json')


@bp.route('/census/<string:table_name>/<string:entity_id>')
def census(table_name,entity_id):
    """Get entity by entity id."""
    print('/census/ table_name: ', table_name, 'entity_id: ', entity_id)
    try:
        table_name_arr = table_name.split('.')
        measurement = table_name_arr[0]
        ent_type_group = table_name_arr[1]
        time_group = table_name_arr[2]
    except:
        return Response(json.dumps('Invalid table name'), mimetype='application/json', status=400)
    
    gig_table = GIGTable(measurement, ent_type_group, time_group)
    entity = Ent.from_id(entity_id)
    census = entity.gig(gig_table)
    
    return Response(census.to_json() ,mimetype='application/json')

@bp.route('/geo/<string:region_id>')
def geo(region_id):
    """Get Geo by region id."""
    print('/geo/ region_id: ', region_id)
    return Response(json.dumps(Ent.geo(region_id)), mimetype='application/json')


@bp.route('/latlng_to_region/<string:latlng_str>')
def latlng_to_region(latlng_str):
    """Get regions by coordinates."""
    print('/latlng_to_region/ latlng_str: ', latlng_str)
    return Response(json.dumps(Ent.latlng_to_region(latlng_str)), mimetype='application/json')

