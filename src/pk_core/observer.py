# -*- encoding: utf-8 -*-
from __future__ import (
    absolute_import,
    print_function, division,
    unicode_literals
)

__all__ = [ 'IObserver', 'IObservable', 'Observable' ]

import abc

# compatible with Python 2.x *and* 3.x
ABC = abc.ABCMeta(str('ABC'), (object,), { '__slots__' : ()})

# --- INTERFACES -----------------------------------------------

class IObserver(ABC) :

    @abc.abstractmethod
    def observe(self, *args, **kwargs) :
        pass

class IObservable(ABC) :
    
    @abc.abstractmethod
    def add_observer(self, observer) :
        pass

    @abc.abstractmethod
    def remove_observer(self, observer) :
        pass

    @abc.abstractmethod
    def remove_all_observers(self) :
        pass

    @abc.abstractmethod
    def notify(self, *args, **kwargs) :
        pass

# --- IMPLEMENTATIONS -------------------------------------------

class Observable(IObservable) :

    def __init__(self) :
        self._observers = set()

    def add_observer(self, observer) :
        if not isinstance(observer, IObserver) :
            raise ValueError(
                "{} : don't respect interface IObserver".format(
                    observer
                )
            )
        self._observers.add(observer)

    def remove_observer(self, observer) :
        self._observers.remove(observer)

    def remove_all_observers(self) :
        self._observers.clear()

    def notify(self, *args, **kwargs) :
        for observer in self._observers :
            observer.observe(*args, **kwargs)
            
