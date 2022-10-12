from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.product import Product
from models.maker import Maker

import repositories.maker_repository as maker_repository
import repositories.product_repository as product_repository  # Keep an eye on the order

products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products) # this could go into /  and homepage

################################################################

@products_blueprint.route("/products/new", methods=['GET']) 
def new_product():
    products = product_repository.select_all()
    makers = maker_repository.select_all() 
    return render_template("products/new.html", products = products) #makers = makers

@products_blueprint.route("/products/", methods=['POST'])
def add_product():
    ### would ID be in here? isnt ID automatically generated? 
    name = request.form['name']
    purchase = request.form['purchase']
    sell = request.form['sell']
    description = request.form['description']
    stock_qty = request.form['stock_qty']

    maker_id =request.form['maker']
    maker = maker_repository.select(maker_id)
    
    product_repository.save(products)
    return redirect("/products")

################################################################

@products_blueprint.route("/products/<id>")
def show(id):
    products = product_repository.select(id)
    maker = product_repository.makers(products)
    return render_template("products/show.html", products=products, maker=maker)

@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    products = product_repository.select(id)
    maker = maker_repository.select_all()
    return render_template("product/edit.html", products=products, maker=maker)

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')
