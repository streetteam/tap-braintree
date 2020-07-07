import datetime

import pytz

from . import utils


class InvalidData(Exception):
    """Raise when data doesn't validate the schema"""


def transform_row(row, schema):
    return _transform_field(row, schema)


def _anyOf(data, schema_list):
    for schema in schema_list:
        try:
            return _transform_field(data, schema)
        except:
            pass

    raise InvalidData("{} doesn't match any of {}".format(data, schema_list))


def _array(data, items_schema):
    return [_transform_field(value, items_schema) for value in data]


def _object(data, properties_schema):
    return {
        field: _transform_field(getattr(data, field), field_schema)
        for field, field_schema in properties_schema.items()
        if hasattr(data, field)
    }


def _type_transform(value, type_schema):
    if isinstance(type_schema, list):
        for typ in type_schema:
            try:
                return _type_transform(value, typ)
            except:
                pass

        raise InvalidData("{} doesn't match any of {}".format(value, type_schema))

    if not value:
        if type_schema != "null":
            raise InvalidData("Null is not allowed")
        else:
            return None

    if type_schema == "string":
        return str(value)

    if type_schema == "integer":
        return int(value)

    if type_schema == "number":
        return float(value)

    if type_schema == "boolean":
        return bool(value)

    raise InvalidData("Unknown type {}".format(type_schema))


def _transform_field(value, field_schema):
    if "anyOf" in field_schema:
        return _anyOf(value, field_schema["anyOf"])

    if field_schema["type"] == "array":
        return _array(value, field_schema["items"])

    if field_schema["type"] == "object":
        return _object(value, field_schema["properties"])

    # Ordering of isinstance datetime checks matters
    # must check datetime.datetime first or it matches against datetime.date
    if isinstance(value, datetime.datetime):
        value = utils.strftime(value.replace(tzinfo=pytz.UTC))

    if isinstance(value, datetime.date):
        dt = datetime.datetime(value.year, value.month, value.day, tzinfo=pytz.UTC)
        value = utils.strftime(dt)

    value = _type_transform(value, field_schema["type"])

    return value
