import contextlib

from connection import Connection


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn.start_transaction()

    def commit(self):
        self.conn.commit_transaction(self.xid)

    def rollback(self):
        self.conn.rollback_transaction(self.xid)


class StartTransaction:

    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        self.tx = Transaction(self.conn)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.tx.commit()
        else:
            self.tx.rollback()
            return False


@contextlib.contextmanager
def start_transaction(conn):
    tx = Transaction(conn)

    try:
        yield tx

    except Exception:
        tx.rollback()
        raise

    tx.commit()


conn_1 = Connection()
try:
    with start_transaction(conn_1) as tx:
        x = 1 + 1
        raise ValueError()
        y = x + 2
        print('transaction 0 =', x, y)
except ValueError:
    print('Ops! Transaction 0 failed!')

