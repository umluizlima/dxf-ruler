import os.path
from subprocess import check_output
from flask import (
    Blueprint, send_file
)

bp = Blueprint('api', __name__)


@bp.route('/<int:length>')
def ruler(length):
    """Generate and send ruler of given length."""
    filename = os.path.basename(check_output(
        ['dxf-ruler-generator', f'{length}']
    ).decode('utf-8'))
    return send_file(
        os.path.abspath(filename),
        as_attachment=True
    )
