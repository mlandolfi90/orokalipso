import frappe
from erpnext.setup.doctype.currency_exchange.currency_exchange import CurrencyExchange
from frappe.model.document import Document

class orokalipsoExchange(CurrencyExchange):
	def validate(self):
		print ("\n\n\n   CODIGO PERSONALIZADO... \n\n\n")
		return