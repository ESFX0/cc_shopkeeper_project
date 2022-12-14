# from multiprocessing import AuthenticationError
from db.run_sql import run_sql

# from repositories import maker_repository
# from repositories import product_repository

from models.maker import Maker  # 1.2many
from models.product import Product



# SAVE
def save(maker):
    sql = """
    INSERT INTO makers (name, address)
    VALUES (%s, %s) RETURNING *
    """
    values = [maker.name, maker.address]
    results = run_sql(sql, values)
    id = results[0]['id']    
    maker.id = id
    #maker.id = results[0]['id']
    return maker

# SELECT ALL
def select_all():
    makers = []

    sql = "SELECT * FROM makers"
    results = run_sql(sql)
    for row in results:
        #product = product_repository.select(row['product_id'])
        maker = Maker(row['name'], row['address'], row['id'])
        makers.append(maker)
    return makers

# SELECT MAKER ID
def select(id):
    maker = None
    sql = "SELECT * FROM makers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        result = results[0]
        maker = Maker(result['name'], result['address'], result['id'])
    return maker

# DELETE ALL
def delete_all():
    sql = "DELETE FROM makers"
    run_sql(sql)

# DELETE WITH ID ONLY
def delete(id):
    sql = "DELETE FROM makers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE MAKER
def update(makers):
    sql = "UPDATE makers SET (name, address) = (%s, %s) WHERE id = %s"
    values = [makers.name, makers.address, makers.id]
    run_sql(sql, values)