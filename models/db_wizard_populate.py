from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.t_registro_clima,10)
