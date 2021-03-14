from app.errors import E_404, E_500
from app.lru_cache import LRUCache
from flask import abort, request
from flask_restplus import Namespace, Resource, fields

CACHE_CAPACITY = 3

lru_cache = LRUCache(capacity=CACHE_CAPACITY)
cache_api = Namespace("cache", description="Cache operations")


@cache_api.route("/<string:key>")
class CacheRouter(Resource):
    value_model = cache_api.model(
        "CacheValue",
        {
            "value": fields.String(
                required=True, description="Value to cache", example="CACHE VALUE"
            )
        },
    )

    def get(self, key: str):
        try:
            return {key: lru_cache.get(key)}
        except KeyError:
            abort(404, E_404)
        except Exception as e:
            abort(500, E_500)

    @cache_api.expect(value_model, validate=True)
    def post(self, key: str):
        try:
            value = request.json["value"]
            lru_cache.set(key, value)
            return {key: value}
        except Exception as e:
            abort(500, E_500)

    def delete(self, key: str):
        try:
            return {key: lru_cache.delete(key)}
        except KeyError:
            abort(404, E_404)
        except Exception as e:
            abort(500, E_500)
