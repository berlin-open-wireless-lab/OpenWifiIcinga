from setuptools import setup, find_packages

setup(
    name='OpenWifiIcinga',
    version="0.1",
    description="Testplugin for OpenWifi",
    author="Johannes Wegener",
    install_requires=["OpenWifi", "pycinga"],
    entry_points="""
    [OpenWifi.plugin]
    addPluginRoutes=OpenWifiIcinga:addPluginRoutes
    models=OpenWifiIcinga:modelString
    globalPluginViews=OpenWifiIcinga:configOpenWifiIcinga
    onDeviceRegister=OpenWifiIcinga:addToIcinga
    """,
    packages=find_packages(),
    include_package_data=True,
)
