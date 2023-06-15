from flask import Blueprint, Response
from application.api.mylocal.gig.Ent import Ent
from application.api.mylocal.gig.GIGTable import GIGTable
import json

bp = Blueprint('mylocal', __name__)
url_prefix = '/mylocal_server'

@bp.route('/')
def index():
    """Index."""
    data = 'mylocal_server Running.!'
    return data

@bp.route('/entity/<string:entity_id>')
def entity(entity_id):
    """Get entity by entity id."""
    entity = Ent.from_id(entity_id)
    return Response(json.dumps(str(entity)), mimetype='application/json')


@bp.route('/census/<string:table_name>/<string:entity_id>')
def census(table_name,entity_id):
    """Get entity by entity id."""
    table_name_arr = table_name.split('.')
    measurement = table_name_arr[0]
    ent_type_group = table_name_arr[1]
    time_group = table_name_arr[2]

    gig_table = GIGTable(measurement, ent_type_group, time_group)
    entity = Ent.from_id(entity_id)
    print(entity.gig(gig_table))
    census = entity.gig(gig_table)

    return Response(json.dumps(str(census)), mimetype='application/json')

@bp.route('/geo/<string:region_id>')
def geo(region_id):
    """Get entity by entity id."""
    entity = Ent.from_id(region_id)
    return Response(json.dumps(Ent.geo(entity)), mimetype='application/json')

