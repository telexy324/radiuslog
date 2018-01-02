from flask import _app_ctx_stack, abort, current_app, request
from pagination import Pagination
from flask_pymongo import ASCENDING
from . import db
from . import utils


def paginate(ipaddress, blimit, tlimit, page=None, per_page=None, error_out=True, max_per_page=None):


    if request:
        if page is None:
            try:
                page = int(request.args.get('page', 1))
            except (TypeError, ValueError):
                if error_out:
                    abort(404)

                page = 1

        if per_page is None:
            try:
                per_page = int(request.args.get('per_page', 10))
            except (TypeError, ValueError):
                if error_out:
                    abort(404)

                per_page = 10
    else:
        if page is None:
            page = 1

        if per_page is None:
            per_page = 20

    if max_per_page is not None:
        per_page = min(per_page, max_per_page)

    if page < 1:
        if error_out:
            abort(404)
        else:
            page = 1

    if per_page < 0:
        if error_out:
            abort(404)
        else:
            per_page = 20

    #items = self.limit(per_page).offset((page - 1) * per_page).all()
    userlogst = db.db.user_log.find({'Framed-IP-Address': ipaddress,\
    'Event-Timestamp':{'$gt': int(blimit), '$lt' : int(tlimit)}}).\
    sort('Event-Timestamp',ASCENDING).skip((int(page) - 1) * per_page).limit(per_page)

    with open('/home/1207.txt','wb') as www:
        www.write(str(ipaddress))
        www.write('\n')
        www.write(str(blimit))
        www.write('\n')
        www.write(str(tlimit))
        www.write('\n')
        www.write(str(page))
        www.write('\n')
        www.write(str(per_page))

    items = []
    for xt in userlogst:
        dictrad = {}
        for (kt,vt) in xt.items():
            if kt == 'Event-Timestamp':
                v = utils.timestamp2string(vt)
                dictrad.update({kt:v})
                continue
            else:
                dictrad.update({kt:vt})
                continue
        items.append(dictrad)


    if not items and page != 1 and error_out:
        abort(404)

    # No need to count if we're on the first page and there are fewer
    # items than we expected.
    if page == 1 and len(items) < per_page:
        total = len(items)
    else:
        total = db.db.user_log.find({'Framed-IP-Address': ipaddress,\
        'Event-Timestamp':{'$gt': int(blimit), '$lt' : int(tlimit)}}).count()
        with open('/home/12073.txt','wb') as www:
            www.write(str(int(total)))

    with open('/home/12072.txt','wb') as www:
        www.write(str(page))
        www.write('\n')
        www.write(str(per_page))
        www.write('\n')
        www.write(str(total))
        www.write('\n')

    return Pagination(page, per_page, total, items)

