modelString = 'OpenWifiIcinga.models'
configOpenWifiIcinga = [['icinga', 'Icinga']]

def addPluginRoutes(config):
    config.add_route('icinga', '/icinga')
    return "OpenWifiIcinga"

def addToIcinga(uuid):
    from openwifi.models import OpenWrt, DBSession
    from .models import Icinga
    from pycinga import icinga

    icingaConfig = DBSession.query(Icinga).all()
    if (len(icingaConfig) <= 0):
        print("No icinga configuration - leaving...")
        return

    icingaConnection = icinga(icingaConfig[0].login,
                              icingaConfig[0].password,
                              icingaConfig[0].url,
                              icingaConfig[0].port,
                              icingaConfig[0].verify)

    device = DBSession.query(OpenWrt).get(uuid)

    if (not device):
        print("No Device found...")
        return

    icingaConnection.add_host(uuid, address = device.address,check_command='hostalive')
