# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AnalizarPuro(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.orokalipso.doctype.analizar_puro_item.analizar_puro_item import Analizarpuroitem
		from erpnext.orokalipso.doctype.analizar_puro_pagos.analizar_puro_pagos import Analizarpuropagos
		from frappe.types import DF

		almacen_predeterminado: DF.Link | None
		amended_from: DF.Link | None
		analizar_puro_pagos: DF.Table[Analizarpuropagos]
		apodo: DF.Data | None
		centro_costos: DF.Link | None
		cobro_en_divisas: DF.Check
		cobro_en_virutas: DF.Check
		company: DF.Link | None
		contacto: DF.Link | None
		costo_cero: DF.Check
		credito: DF.Check
		cuenta_de_amortizacion: DF.Link | None
		divisas_predeterminado: DF.Currency
		en_oficina: DF.Check
		entrada_de_pago_relacionada: DF.Link | None
		enviar_msj: DF.Check
		item_predeterminado: DF.Link | None
		item_servicio: DF.Link | None
		items: DF.Table[Analizarpuroitem]
		ley_analitica: DF.Float
		ley_recuperable: DF.Float
		monto_cobrado: DF.Currency
		naming_series: DF.Literal["AINV-.YYYY.-", "AINV-RET-.YYYY.-"]
		nro_de_calculos: DF.Int
		nro_movil: DF.Data | None
		oficina: DF.Literal["", "Calle Miranda", "Calle Van Prag"]
		pendiente: DF.Currency
		peso_fundido: DF.Float
		peso_sin_fundir: DF.Float
		porc_merma: DF.Percent
		posting_date: DF.Date
		posting_time: DF.Time | None
		puras_en_gr: DF.Float
		purchase_invoice: DF.Link | None
		saldo_cliente: DF.Currency
		secuencia_maquina: DF.Int
		set_posting_time: DF.Check
		supplier: DF.Link
		supplier_name: DF.Data | None
		title: DF.Data | None
		viruta_predeterminado: DF.Float
		virutas_cobradas: DF.Float
	# end: auto-generated types
	pass
