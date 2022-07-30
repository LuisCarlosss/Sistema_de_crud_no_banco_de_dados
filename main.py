import crudMysql
import eventRecorder

if crudMysql.checkDatabaseConnection() == False:
    print('Connection error')
else:
    print(crudMysql.checkDatabaseConnection())
    command = str(input('Type your commands here, Any doubt type help\n> ')).lower()


    if command == 'query':
        crudMysql.queryEntireTable()
        eventRecorder.getDataAndTime()
        eventRecorder.recordTheEvents('query data')

    elif command == 'insert':
        crudMysql.insertDataInTable()
        eventRecorder.getDataAndTime()
        eventRecorder.recordTheEvents('enter data')

    elif command == 'update':
        crudMysql.updateDataInTheTable()
        eventRecorder.getDataAndTime()
        eventRecorder.recordTheEvents('Update data')

    elif command == 'delete':
        crudMysql.deleteDataInTable()
        eventRecorder.getDataAndTime()
        eventRecorder.recordTheEvents('Deleted dada')

    elif command == 'help':
        crudMysql.commandList()

    elif command == 'exit':
        pass
    else:
        print('invalid command retype')


