import sqlalchemy
import sys

VERSION = 0.2

def welcome_msg():
    print(f'\nWelcome to db-browser version {VERSION}\n\n')

def input_db_path():
    # retrive db path provided as a argument
    db_path = sys.argv[1]
    return db_path

def print_results(result):
    '''
    result : ResultProxy
    '''
    for row in result:
        print(row)

    # print empty line
    print('')

def run_queries(engine):
    while True:
        query = input('> ')
        if not query: break
        result = engine.execute(query)
        print_results(result)
    
    print('end')

def show_table(table):
    print(table.name)
    for column in table.c:
        print(f'\t{column.name}')

    # print blankline
    print() 

def show_schema(engine):
    metadata = sqlalchemy.MetaData()
    metadata.reflect(bind=engine)

    print('## TABLES\n')

    for table in metadata.tables.values():
        show_table(table)


def main():
    welcome_msg()

    db_path = input_db_path()
    engine = sqlalchemy.create_engine(db_path)

    show_schema(engine)
    run_queries(engine)


main()
