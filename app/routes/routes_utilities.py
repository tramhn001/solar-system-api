from flask import abort, make_response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        abort(make_response({"message": f"{cls.__name__} with {model_id} is invalid"}, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        abort(make_response({"message": f"{cls.__name__} with {model_id} is not found"}, 404))
    
    return model