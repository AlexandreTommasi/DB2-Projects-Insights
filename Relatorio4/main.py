from database import Database
from helper.writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer


db = Database(database="mercado", collection="compras")
#db.resetDatabase()

# 1- Média de gasto total:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
])

writeAJson(result, "Média de gasto total")

# 2- Cliente que mais comprou em cada dia:
result = db.collection.aggregate([
     {"$unwind": "$produtos"},
     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
     {"$sort": {"_id.data": 1, "total": -1}},
     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])

writeAJson(result, "Cliente que mais comprou em cada dia")

# 3- Produto mais vendido:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result, "Produto mais vendido")

analyzer = ProductAnalyzer(db.collection)

# Total de vendas por dia
analyzer.total_sales_per_day()

# Cliente que mais comprou em cada dia
analyzer.most_sold_product_per_day()

# Cliente que mais gastou em uma única compra
analyzer.customer_highest_spending()

# Produtos vendidos acima de uma certa quantidade
quantity_threshold = 1  # Define o limiar de quantidade conforme necessário
analyzer.products_sold_above_quantity(quantity_threshold)