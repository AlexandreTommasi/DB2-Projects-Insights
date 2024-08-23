from pymongo.collection import Collection
from helper.writeAJson import writeAJson


class ProductAnalyzer:
    def __init__(self, db_collection: Collection):
        self.db_collection = db_collection

    def total_sales_per_day(self):
        result = self.db_collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": 1}}},
            {"$sort": {"_id": 1}}
        ])
        writeAJson(list(result), "Total de vendas por dia")

    def most_sold_product_per_day(self):
        result = self.db_collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ])
        writeAJson(list(result), "Cliente que mais comprou em cada dia")

    def customer_highest_spending(self):
        result = self.db_collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        writeAJson(list(result), "Cliente que mais gastou em uma única compra")

    def products_sold_above_quantity(self, quantity_threshold: int):
        result = self.db_collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": quantity_threshold}}},
            {"$group": {"_id": "$produtos.descricao"}}
        ])
        writeAJson(list(result), "Produtos vendidos acima de uma certa quantidade")
