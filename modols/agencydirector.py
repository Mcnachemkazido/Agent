
class AgencyDirector:
    _instance = None

    def __new__(cls,name_admin):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name_admin = name_admin
        return cls._instance
a = AgencyDirector("menachem")
