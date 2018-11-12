# -*- encoding: utf-8 -*-
from __future__ import (
    absolute_import, print_function, division,
    unicode_literals
)

try :
    import tkinter
    from tkinter import messagebox
except ImportError :
    import Tkinter as tkinter
    import tkMessageBox as messagebox


class Dialogs :

    __shared_state = {}

    def __init__(self) :
        self.__dict__ = self.__shared_state
        self.make_root()

    def make_root(self) :
        try :
            if self.root is not None :
                return
        except AttributeError :
            pass

        self.auto = True
        self.root = tkinter.Tk()
        self.root.withdraw()

    def change_root(self, new_root) :
        try :
            if self.auto :
                self.root.destroy()
                self.root = None
        except AttributeError :
            pass

        self.auto = False
        self.root = new_root
        

    def format_message(self, msg) :
        message = str(msg)
        if isinstance(msg, BaseException) :
            message = '{} : {}'.format(
            msg.__class__.__name__,
            ' '.join(map(str, msg.args))
        )

        return message
    
    def error(self, msg, title='Error') :
        message = self.format_message(msg)
        messagebox.showerror(
            title=title,
            message=message,
            parent = self.root
        )

    def warning(self, msg, title='Warning') :
        message = self.format_message(msg)
        messagebox.showwarning(
            title=title,
            message=message,
            parent = self.root
        )
        
    def info(self, msg, title='Info') :
        message = self.format_message(msg)
        messagebox.showinfo(
            title=title,
            message=message,
            parent = self.root
        )
        
    def question(self, question, title='Question') :
        message = str(question)
        return messagebox.askquestion(
            title=title,
            message=message,
            parent = self.root
        )

    def okcancel(self, question, title='Question') :
        message = str(question)
        return messagebox.askokcancel(
            title=title,
            message=message,
            parent = self.root
        )

    def retrycancel(self, question, title='Question') :
        message = str(question)
        return messagebox.askretrycancel(
            title=title,
            message=message,
            parent = self.root
        )

    def yesno(self, question, title='Question') :
        message = str(question)
        return messagebox.askyesno(
            title=title,
            message=message,
            parent = self.root
        )
