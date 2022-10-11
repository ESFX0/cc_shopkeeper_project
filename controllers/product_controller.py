from flask import Flask, render_template # request, redirect
from flask import Blueprint

from models.product import Product
from models.maker import Maker

import repositories.maker_repository as maker_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

# makers_blueprint = Blueprint("makers", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

# @makers_blueprint.route("/makers")
# def makers():
#     makers = maker_repository.select_all()
#     return render_template("makers/index.html", makers = makers)
