# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    dian_type = fields.Selection(
        selection_add=[
            ('e-invoicing', _('E-Invoicing')),
            ('e-credit_note', _('E-Credit Note')),
            ('e-debit_note', _('E-Debit Note')),
            ('e-support_document', _('E-Support Document')),
            ('e-support_document_credit_note', _('E-Support Document Credit Note')),
            ('contingency_checkbook_e-invoicing', _('Contingency Checkbook E-Invoicing'))])
