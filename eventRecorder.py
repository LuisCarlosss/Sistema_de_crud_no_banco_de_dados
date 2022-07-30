def getDataAndTime():
    global dataTime
    import time
    getLocalTime = time.localtime()
    dataTime = f'Data > {getLocalTime [2]}/{getLocalTime [1]}/{getLocalTime [0]}, hours > {getLocalTime [3]}:{getLocalTime [4]}:{getLocalTime [5]}'
    return dataTime


def recordTheEvents(event):
    getDataAndTime()
    with open('records.txt','a') as file:
        file.write(f'{dataTime}     {event}  \n')


if __name__ == '__main__':
    recordTheEvents('test')