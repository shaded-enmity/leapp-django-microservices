""" """

from collections import namedtuple

from leapp import get_actor_input


DatabaseInfo = namedtuple('DatabaseInfo', ['name', 'username', 'password'])


def data_export_cmd(db_conn):
    cmd = 'sudo -u {s_user} PGPASSWORD={d_password} pg_dump -F t -U {d_user} {d_name}'
    fmt = {
        's_user': 'postgres',
        'd_user': db_conn.username,
        'd_name': db_conn.name,
        'd_password': db_conn.password
    }
    return cmd.format(**fmt)


def data_import_cmd(db_conn):
    cmd = 'pg_restore -C -d postgres -F t && psql -c "ALTER USER {} PASSWORD \'{}\';"'
    return cmd.format(db_conn.username, db_conn.password)
