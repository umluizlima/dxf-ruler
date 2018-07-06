from subprocess import check_output
from flask import (
    Blueprint, send_file
)

bp = Blueprint('api', __name__)


@bp.route('/<int:length>')
def ruler(length):
    """Generate and send ruler of given length."""
    filepath = check_output(
        f'dxf-ruler-generator {length}'
    ).decode('utf-8')
    return send_file(
        filepath,
        as_attachment=True
    )
