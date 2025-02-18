vendas = [100,68,97,45,4,75,89,67,66,49,523,112,108,63,200,23,12,18]
meta = 100
qtda_bateu_meta = 0
for venda in vendas:
    if venda >= meta:
        qtda_bateu_meta += 1
qtde_funcionarios = len(vendas)
print("O percentual de pessoas que bateram a meta foi de {:.1%}" .format(qtda_bateu_meta/qtde_funcionarios))