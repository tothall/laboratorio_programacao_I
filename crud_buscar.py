from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from crud_editar import editar
from crud_deletar import deletar
import time

def buscar(portfolio, placa):
    while True:
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            funcao_exibir(veiculo)
            op = input('EDITAR [1]\nEXCLUIR [2]\nNOVA BUSCA [3]\nVOLTAR AO MENU [4]\n>>> ')
            match op:
                case '1':
                    editar(portfolio, placa)
                    break
                case '2':
                    deletar(portfolio, placa)
                    break
                case '3':
                    placa = input('PLACA: ')
                    continue
                case '4':
                    return
                case _:
                    print('ERRO: opcao invalida!')
                    time.sleep(1)
        else:
            print('ERRO: Veículo não encontrado!')
            while True:
                n = input('NOVA BUSCA [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    placa = input('PLACA: ')
                    break  
                elif n == '2':
                    return 
                else:
                    print('ERRO: Opção inválida!')
                    time.sleep(1)