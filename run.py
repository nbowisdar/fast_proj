from src.database.tablse import create_tables
from src.pars_test import main


if __name__ == '__main__':
    create_tables()
    print('Start parsing...')
    main()
