from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .forms import IpQueryForm
from flask_pymongo import ASCENDING
from .. import utils
from .. import db
from flask_paginate import Pagination, get_page_parameter


@main.route('/', methods=['GET', 'POST'])
def index():
    form = IpQueryForm()
    if form.validate_on_submit():

        limit = 10
        #page = request.args.get('page', type=int, default=1)
        skip = request.args.get('skip', type=int, default=0)


        userlogst = db.db.user_log.find({'Framed-IP-Address': form.ipaddress.data,\
            'Event-Timestamp':{'$gt': utils.string2timestamp(form.blimit.data), '$lt' : utils.string2timestamp(form.tlimit.data)}}).\
            sort('Event-Timestamp',ASCENDING).skip(skip).limit(limit)


        #userlogs = db.user_log.find_one_or_404({'Framed-IP-Address': form.ipaddress, 'Event-Timestamp':{'$gt': utils.string2timestamp(form.blimit), '$lt' : utils.string2timestamp(form.tlimit)}}).sort('Event-Timestamp',ASCENDING).skip(skip).limit(limit)
        #user_logs = db.user_log.find({'Framed-IP-Address': form.ipaddress, 'Event-Timestamp':{'$gt': utils.string2timestamp(form.blimit), '$lt' : utils.string2timestamp(form.tlimit)}}).sort('Event-Timestamp',ASCENDING)

        userlogs = []
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
            userlogs.append(dictrad)

        userlogstotal = db.db.user_log.find({'Framed-IP-Address': form.ipaddress.data, 'Event-Timestamp':{'$gt': utils.string2timestamp(form.blimit.data), '$lt' : utils.string2timestamp(form.tlimit.data)}}).count()



        return render_template('show.html', userlogs=userlogs, limit=limit, previous=skip-limit, next=skip+limit)
    return render_template('index.html', form=form)