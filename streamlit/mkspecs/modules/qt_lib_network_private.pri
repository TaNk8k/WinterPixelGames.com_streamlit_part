QT.network_private.VERSION = 5.15.2
QT.network_private.name = QtNetwork
QT.network_private.module =
QT.network_private.libs = $$QT_MODULE_LIB_BASE
QT.network_private.includes = $$QT_MODULE_INCLUDE_BASE/QtNetwork/5.15.2 $$QT_MODULE_INCLUDE_BASE/QtNetwork/5.15.2/QtNetwork
QT.network_private.frameworks =
QT.network_private.depends = core_private network
QT.network_private.uses = openssl
QT.network_private.module_config = v2 internal_module
QT.network_private.enabled_features = openssl-linked openssl linux-netlink system-proxies
QT.network_private.disabled_features = libproxy netlistmgr
QMAKE_INCDIR_GSSAPI = /root/miniconda3/envs/streamlit/include
QMAKE_LIBS_OPENSSL = -lssl -lcrypto
QMAKE_LIBS_NETWORK = 
QMAKE_LIBS_GSSAPI = -L/root/miniconda3/envs/streamlit/lib -lgssapi_krb5
