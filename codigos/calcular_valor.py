def calcula_valor(**kwargs):
    val = kwargs.get('valor')
    impost = kwargs.get('imposto')
    descont = kwargs.get('desconto')
    if impost:
        val += val * (impost / 100)
    if descont:
        val -= descont
    return val
    
#valortotal = calcula_valor(99)
#print(valortotal)

valortotal = calcula_valor(valor=100.0, desconto=5.0)
print(valortotal)

#valortotal = calcula_valor(valor=100.0, imposto=9, desconto=5.0)
#print(valortotal)