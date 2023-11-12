import time 
import BoosT3RColors as BC

colors = BC.colors
prefixes = BC.prefixes

Active = False

class Box:
    
    def __init__(self,
                 msg : str
                 ) -> None:
        self.message = msg
            
    def infoMessageBox(self, time_):
        return f"{colors.white}[{colors.cyan}{time_}{colors.white}] [{prefixes.META_INFO}{colors.white}] {colors.yellow}{self.message}"
    
    def errorMessageBox(self, time_):
        return f"{colors.white}[{colors.cyan}{time_}{colors.white}] [{colors.BackRed}ERROR{colors.white}] {prefixes.GRAY}{self.message}"
    
class Animation:
    
    def ani(msg, for_):
        party = ['<', '_', "^", '>']
        
        if Active:
        
            for i in range(for_):
                for p in party:
                    print(f"\r{msg} {p}", end="")
                    time.sleep(0.08)
                    
        else:
            print(f"{msg}")
            
class Reader:
    
    def __init__(self,
                 fileNameOrPath: str,
                 typeToRead: str = "r"
                 ) -> None:
        self.fp = fileNameOrPath
        self.tr = typeToRead
        
    def read(self):
        try:
            filex = open(self.fp, self.tr)
            return filex.read()
        except Exception as ETR:
            return ETR
        
class exeCuter:
    
    def ec(textToExeCute):
        exec(textToExeCute)
        
    
