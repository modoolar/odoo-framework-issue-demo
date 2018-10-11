[![Build Status](https://travis-ci.com/modoolar/odoo-framework-issue-demo.svg?branch=11.0)](https://travis-ci.com/modoolar/odoo-framework-issue-demo)

This module demonstrates case when module extends a model with
required Many2one field to newly defined model. This scenario
leads to sql bad query errors when installing module on db with
existing records, because not null constraint can not be added.

Look at logs on travis tests that are failing.
