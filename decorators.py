def log(func):
    """decorator for log function in log.txt("""
    def getdate():
        import datetime
        return str(datetime.datetime.now())
    def inner(*args):
        f = open("log.txt", "a")
        f.write("["+getdate()+"]\n")
        f.write("     start: " + func.__name__ + "\n")
        f.write("         return : "+str(func(*args)))
        f.write("\n     end: " + func.__name__ + "\n")
        f.close()
        return func(*args)
    return inner

def debuglog(func):
    def innner(*args):
        return func(*args)

def debug(func):
    def inner(*args):

        return func(*args)
