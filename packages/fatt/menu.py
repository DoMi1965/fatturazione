class Menu(object):
    def config(self, root):
        root.packageBranch("System", pkg='sys', tags="admin")
        root.packageBranch("Admin", pkg='adm', tags="admin")
        root.packageBranch("Glbl", pkg='glbl', tags="admin,backoffice")
        
        fat = root.branch('Fatturazione')
        fat_main = fat.branch('Menu Principale')
        # fat_main.thpage('Cliente', table='rcweb.cliente', tags="admin,backoffice")
