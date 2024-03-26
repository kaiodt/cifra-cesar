# Cifra de César

A ideia deste projeto é representar uma biblioteca capaz de executar a **Cifra de César** (**ROT13**).

## Exemplos de Uso

### Encriptação

```python
from cesar import encripta

encripta('Kaio')  # xnvb
```

### Decriptação

```python
from cesar import decripta

encripta('xnvb')  # kaio
```

### Rotações Diferentes de 13

```python
from cesar import decripta, encripta

encripta('Kaio', 14)  # yowc
decripta('yowc', 14)  # kaio
```
