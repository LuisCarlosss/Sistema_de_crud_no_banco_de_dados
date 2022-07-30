import mysql.connector


accountSetup = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'cadastro'
}

def checkDatabaseConnection():
    try:
        global connection,cursor
        connection = mysql.connector.connect(**accountSetup)
        cursor = connection.cursor()
        
    except:
        return False
    else:
        return True


def commint():
    connection.commit()

def queryEntireTable():    

    wholeTable = '''SELECT * FROM pessoa;'''
    cursor.execute(wholeTable)

    data = cursor.fetchall()
    if data == []:
        print('database are empty')
    else:
        for line in data:
            print(line)
            


def insertDataInTable():
    print('Enter the data you want to insert into the database')
    name = str(input('Name > ')).capitalize()
    birthDate = str(input('BirtDate(ex : 1860,05,28) > '))
    genre = str(input('Genre(type M or F) > ')).upper()
    height = float(input('Height(ex:1.80) > '))
    weith = float(input('Weith > '))
    nationality = str(input('nationality > ')).capitalize()

    commandInsert = f'''INSERT INTO pessoa VALUES
    (DEFAULT,'{str(name)}','{str(birthDate)}','{str(genre)}','{str(height)}','{str(weith)}','{str(nationality)}');'''
    cursor.execute(commandInsert)
    commint()
    print('Data inserted into the database')

def updateDataInTheTable():
    column = ['nome','nascimento','sexo','altura','peso','nacionalidade']
    print(column)
    inputColumn = str(input('What do you want to Update?\n> '))
    newData = str(input('Enter Update >'))
    personId = str(input('Enter the id if the person you want to update > '))
    commandUpdate = f'''UPDATE pessoa
    SET {inputColumn} = '{newData}'
    WHERE id = '{personId}';
    '''
    cursor.execute(commandUpdate)
    commint()
    print('Data update')


def deleteDataInTable():
    personId = str(input('Enter the id of the person you want to delete from the database\n> '))
    commandDelete = f'''
    DELETE FROM pessoa
    WHERE id = {personId};  '''
    cursor.execute(commandDelete)
    commint()
    print('Data delete from database')


commands = {
    '[query]':'> Show table',
    '[insert]':'> Insert data in table',
    '[update]':'> Update data in table',
    '[delete]':'> Delete data in table',
    '[exit]': '> Close system',
    '[help]':'show commands'
}

def commandList():
    print('system commands\n')
    for command,meaning in commands.items():
        print(command,meaning,'\n')
    print('\ntype help to display this message again')

