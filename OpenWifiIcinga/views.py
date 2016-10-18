from OpenWifiIcinga.forms import IcingaConfForm
from openwifi.models import DBSession
from .models import Icinga
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='icinga', renderer='templates/icingaConf.jinja2', layout='base', permission='view')
def icingaConf(request):
    form = IcingaConfForm(request.POST)
    if request.method == 'POST' and form.validate():
        icingaConfig = DBSession.query(Icinga).all()
        if len(icingaConfig) > 0:
            icingaConfig[0].login = form.login.data
            icingaConfig[0].password = form.password.data
            icingaConfig[0].url = form.url.data
            icingaConfig[0].port = form.port.data
            icingaConfig[0].verify = form.verify.data
        else:
            newConfig = Icinga(form.url.data,
                               form.login.data,
                               form.password.data,
                               form.port.data,
                               form.verify.data)
            DBSession.add(newConfig)

        return HTTPFound(location=request.route_url('home'))
    else:
        icingaConfig = DBSession.query(Icinga).all()
        if len(icingaConfig) > 0:
            form.login.data = icingaConfig[0].login
            form.password.data = icingaConfig[0].password
            form.port.data = icingaConfig[0].port
            form.url.data = icingaConfig[0].url
            form.verify.data = icingaConfig[0].verify

    save_url = request.route_url('icinga')
    return {'save_url':save_url, 'form':form}
