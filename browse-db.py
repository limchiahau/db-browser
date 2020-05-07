import sqlalchemy
import sys

VERSION = 0.1

def welcome_msg():
    print(f'Welcome to db-browser version {VERSION}\n\n')

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

def main():
    welcome_msg()

    db_path = input_db_path()
    engine = sqlalchemy.create_engine(db_path)

    run_queries(engine)


main()
