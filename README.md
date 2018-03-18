# Practica 2 TDD

Practica para uso de test y desarrollo siguiendo TDD donde en el producto desarrollado se separa por palabras y cuenta cuantas veces aparece en un texto

## How it works

You can install the dependencies using:

```bash
make bootstrap
```

And execute the tests with:

```bash
make test
```

You can execute the program using the next command:

```bash
python TextDataMiner.py <texto> <stopWordsPath>

python main.py "esto es un texto" "sample\stop_words.txt"
# [[esto, 1], [texto, 1]]
```
