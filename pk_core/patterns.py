# -*- encoding : utf-8 -*-

__all__ = [ 'singleton', 'Borg' ]

# --------------------------------------------------------------------

def singleton(cls) :
    """ singleton as a class decorator
    """
    instances = {}

    # closure
    def getinstance(*args, **kwargs) :
        if cls not in instances :
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance

# --------------------------------------------------------------------

class Borg(object) :
    """ Borg
    """
    __namespace__ = ''
    __shared_state = {}
    
    def __new__(cls, *args, **kwargs) :
        self = object.__new__(cls)
        self.__dict__ = cls.__shared_state.setdefault(cls.__namespace__, {})
        return self

# --------------------------------------------------------------------
