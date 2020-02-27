# -*- coding: utf-8 -*-

from flask_rest_jsonapi.api import Api
from flask_rest_jsonapi.resource import ResourceList, ResourceDetail, ResourceRelationship
from flask_rest_jsonapi.exceptions import JsonApiException

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

__all__ = [
    'Api',
    'ResourceList',
    'ResourceDetail',
    'ResourceRelationship',
    'JsonApiException'
]
