from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .forms import IpQueryForm, MyForm
from flask_pymongo import ASCENDING
from .. import utils
from .. import db
from .. import pagination
from .. import mongoquery


@main.route('/', methods=['GET', 'POST'])
def index():
    form = IpQueryForm()

    with open('/home/1205.txt','wb') as www:
        www.write(str(form.ipaddress.data))
        www.write(str(form.blimit.data))
        www.write(str(form.tlimit.data))

    if form.validate_on_submit():
        with open('/home/1206.txt','wb') as xxx:
            xxx.write(str(form.ipaddress.data))
            xxx.write(str(form.blimit.data))
            xxx.write(str(form.tlimit.data))
        iphandle = form.ipaddress.data
        bhandle = utils.string2timestamp(form.blimit.data)
        thandle = utils.string2timestamp(form.tlimit.data)
        return redirect(url_for('.log', ipaddressinit=iphandle, blimitinit=bhandle, tlimitinit=thandle))
        #return redirect(url_for('.log'),code=307)
    return render_template('index.html', form=form)


#@main.route('/log/<string:ipaddressinit>/<string:blimitinit>/<string:tlimitinit>', methods=['GET'])
#@main.route('/log', methods=['POST'])
#def log(ipaddressinit,blimitinit,tlimitinit):
@main.route('/log', methods=['POST','GET'])
def log():


    if request.method == 'POST':
        ipaddress = request.form.get('ipaddress')
        blimit = request.form.get('blimit')
        tlimit = request.form.get('tlimit')
        page = int(request.form.get('page',1))
        with open('/home/1129.txt','wb') as www:
            www.write(str(ipaddress))
            www.write(str(blimit))
            www.write(str(tlimit))
            www.write(str(page))

    else:
        ipaddress = request.args.get('ipaddressinit')
        blimit = request.args.get('blimitinit')
        tlimit = request.args.get('tlimitinit')
        page = 1


    per_page = 10


    pagination= mongoquery.paginate(ipaddress,blimit,tlimit,page, per_page=per_page,error_out=False)

    userlogs = pagination.items


    return render_template('show.html', userlogs=userlogs, pagination=pagination, ipaddress=ipaddress, blimit=blimit, tlimit=tlimit)


@main.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('index1204.html')


@main.route('/cs', methods=('GET', 'POST'))
def cs():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('cs.html', form=form)