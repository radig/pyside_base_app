# -*- coding: utf-8 -*-

from elixir import *

class User(Entity):
    using_options(tablename='users')
    
    name = Field(Unicode(30))
    lastname = Field(Integer)
    phone = Field(Unicode(30))
    description = Field(UnicodeText)
    
    def __repr__(self):
            return "<User '%s' '%s', '%s'>" % (self.name, self.lastname, self.phone)
