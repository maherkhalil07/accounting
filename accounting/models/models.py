# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError
from odoo.addons.base.models.res_bank import sanitize_account_number
from odoo.tools import remove_accents
import logging
import re

_logger = logging.getLogger(__name__)

# Inherit account journal to translate its name
class AccountJournal(models.Model):
    _inherit = 'account.journal'

    name = fields.Char(string='Journal Name', required=True, translate=True)



#Inherit account COA to translate its name
class AccountAccount(models.Model):
    _inherit = "account.account"

    name = fields.Char(string="Account Name", required=True, index=True, translate=True)
