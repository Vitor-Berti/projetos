from colorama import Fore, Style    
def situaçao_reservatorio(nivel):
    if nivel == 1:
        return (Fore.RED + "Muito Baixo (crítico)")
    elif nivel == 2:
        return (Fore.YELLOW + "Baixo")
    elif nivel == 3:
        return (Fore.GREEN + "Médio")
    elif nivel == 4:
        return (Fore.CYAN + "Alto")
    elif nivel == 5:
        return (Fore.BLUE + "Muito Alto (alerta)")
resp = int(input("Digite o nível do reservatório:"))
print(situaçao_reservatorio(resp))
print(Style.RESET_ALL)
