from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView
from flask_appbuilder.widgets import ListBlock, ShowBlockWidget

from . import appbuilder, db
from .models import Product, ProductType, Rodic, Dyte

class ProductPubRodic(ModelView):
    datamodel = SQLAInterface(Rodic)

class ProductPubDyte(ModelView):
    datamodel = SQLAInterface(Dyte)
    list_widget = ListBlock
    show_widget = ShowBlockWidget


class ProductPubView(ModelView):
    datamodel = SQLAInterface(Product)
    base_permissions = ["can_list", "can_show"]
    list_widget = ListBlock
    show_widget = ShowBlockWidget



    list_columns = ["name","rok_label"]
    search_columns = ["name", "rok"]

    show_fieldsets = [
        ("Summary", {"fields": ["name", "rok_label"]}),
    ]


class ProductView(ModelView):
    datamodel = SQLAInterface(Product)


class ProductTypeView(ModelView):
    datamodel = SQLAInterface(ProductType)
    related_views = [ProductView]


db.create_all()
appbuilder.add_view(ProductPubView, "Our Products", icon="fa-folder-open-o")
appbuilder.add_view(
    ProductView, "List Products", icon="fa-folder-open-o", category="Management"
)
appbuilder.add_separator("Management")
appbuilder.add_view(
    ProductTypeView, "List Product Types", icon="fa-envelope", category="Management"
)
appbuilder.add_separator("Management")
appbuilder.add_view(
    ProductPubRodic, "List rodicu", icon="fa-envelope", category="Management"
)
appbuilder.add_view(
    ProductPubDyte, "List dety", icon="fa-envelope", category="Management"
)
