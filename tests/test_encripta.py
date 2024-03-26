from cifra_cesar.cesar import encripta

def test_encripta_kaio_deve_retornar_xnvb():
    assert encripta('Kaio') == 'xnvb'

def test_encripta_xnvb_deve_retornar_kaio():
    assert encripta('xnvb') == 'kaio'

def test_encripta_deve_retornar_minusculas():
    assert encripta('A').islower()

def test_encripta_deve_preservar_espacos():
    assert encripta('A B')[1] == ' '