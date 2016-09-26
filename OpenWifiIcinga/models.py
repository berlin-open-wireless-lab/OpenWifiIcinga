from openwifi.models import (Base, GUID)

from sqlalchemy import (
        Column,
        Text,
        Integer,
        Boolean
        )

class Icinga(Base):
    __tablename__ = "icingaConfig"
    url = Column(Text, primary_key=True)
    login = Column(Text)
    password = Column(Text)
    port = Column(Integer)
    verify = Column(Boolean)

    def __init__(self, url, login, password, port, verify):
        self.url = url
        self.login = login
        self.password = password
        self.port = port
        self.verify = verify

