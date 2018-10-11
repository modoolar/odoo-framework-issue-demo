from odoo import models, fields, api


class ProjectType(models.Model):
    _name = "project.type"

    name = fields.Char()


class Project(models.Model):
    _inherit = 'project.project'

    @api.model
    def _get_default_type_id(self, ):
        return self.env['ir.model.data'].xmlid_to_res_id(
            "project_type.project_type_software",
            raise_if_not_found=False
        ),

    type_id = fields.Many2one(
        comodel_name="project.type",
        string="Project type",
        required=True,
        default=lambda s: s._get_default_type_id(),
    )
