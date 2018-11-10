# -*- coding: utf-8 -*-

"""
Save ModelItem's to a local SQLite database.
"""

from {{cookiecutter.scraper_name}}.items import ModelItem


class {{cookiecutter.scraper_name}}Pipeline(object):
    def process_item(self, item, spider):
        return item
