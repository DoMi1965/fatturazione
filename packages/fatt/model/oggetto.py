# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('oggetto', pkey='id', name_long='Oggetto', name_plural='Oggetti',caption_field='descrizione')
        self.sysFields(tbl)
        # id, 
        tbl.column('descrizione', name_long='Descrizione', name_short='Descr.')
        tbl.column('note', name_long='Note')
        