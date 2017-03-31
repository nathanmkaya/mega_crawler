from sqlalchemy import create_engine, MetaData, Table
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/topshops')

metadata = MetaData()
shops = Table('nathanmkaya', metadata, autoload=True, autoload_with=engine)


def insert(**kwargs):
    i = shops.insert()
    i.execute(pit_id=kwargs.pit_id,
              portal_id=kwargs.portal_id,
              Kategorie=kwargs.Kategorie,
              Marke=kwargs.Marke,
              co_name=kwargs.co_name,
              co_street=kwargs.co_street,
              co_zip=kwargs.co_zip,
              co_city=kwargs.co_city,
              status=kwargs.status,
              monday_open=kwargs.monday_open,
              monday_close=kwargs.monday_close,
              tuesday_open=kwargs.tuesday_open,
              tuesday_close=kwargs.tuesday_close,
              wednesday_open=kwargs.wednesday_open,
              wednesday_close=kwargs.wednesday_close,
              thursday_open=kwargs.thursday_open,
              thursday_close=kwargs.thursday_close,
              friday_open=kwargs.friday_open,
              friday_close=kwargs.friday_close,
              saturday_open=kwargs.saturday_open,
              saturday_close=kwargs.saturday_close,
              sunday_open=kwargs.sunday_open,
              sunday_close=kwargs.sunday_close)
