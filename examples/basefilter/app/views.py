from flask import g
from flask.ext.appbuilder import ModelView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from app import db, appbuilder
from .models import ContactGroup, Gender, Contact

def get_user():
    return g.user


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)
    list_columns = ['name', 'personal_celphone', 'birthday', 'contact_group.name','created_by.username']
    add_columns = ['name', 'address','birthday','personal_phone','personal_celphone','contact_group','gender']
    edit_columns = ['name', 'address','birthday','personal_phone','personal_celphone','contact_group','gender']
    base_order = ('name', 'asc')
    base_filters = [['created_by', FilterEqualFunction, get_user]]



class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


db.create_all()
appbuilder.add_view(GroupModelView, "List Groups", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(ContactModelView, "List Contacts", icon="fa-envelope", category="Contacts")
appbuilder.add_separator("Contacts")

