import os
import tempfile
import requests

import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
from utils import WWW, JSONFile

from config import GEO_SERVER_URL
from application.api.mylocal.gig.EntType import EntType


class EntGeoMixin:
    @property
    def raw_geo_file(self):
        raw_geo_path = os.path.join(
            tempfile.gettempdir(), f'ent.{self.id}.raw_geo.json'
        )

        return JSONFile(raw_geo_path)

    @property
    def url_remote_geo_data_path(self, endpoint: str):
        id = self.id
        return f'{GEO_SERVER_URL}/{endpoint}/{id}'

    def get_raw_geo(self):
        raw_geo_file = self.raw_geo_file
        if raw_geo_file.exists:
            raw_geo = raw_geo_file.read()
        else:
            raw_geo = WWW(self.url_remote_geo_data_path).readJSON()
            raw_geo_file.write(raw_geo)
        return raw_geo

    def geo(self):
        # url = GEO_SERVER_URL + '/region_geo/LK-11'
        response = requests.get(self.url_remote_geo_data_path('region_geo'))
        if response.status_code == 200:
            data = response.json()
            # Process the response data
        else:
            print('API request failed with status code:', response.status_code)
        return data
