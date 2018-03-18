import sys
from sample.TextDataMiner import Text_Data_Miner

if __name__ == "__main__":
    args = sys.argv[1:]
    if(len(args) == 1):
        resultado = Text_Data_Miner(args[0])
    else:
        resultado = Text_Data_Miner(args[0], args[1])
    print(resultado)
