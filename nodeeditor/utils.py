import traceback

def dumpException(e):
    print("EXCEPTiON:", e)
    traceback.print_tb(e.__traceback__)