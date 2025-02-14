import re
import shodan
from collections import Counter

# Configuração
LOG_FILE = "/root/Projetos/Consulta Shodan/log de rede.txt"
SHODAN_API_KEY = "SUA CHAVE API SHODAN"
TOP_N = 100 # Defina o número de IPs que desejam que sejam consultados. Pode estabelecer um Top 100 IPs mais acessados.
OUTPUT_FILE = "/root/Projetos/Consulta Shodan/shodan_results.txt"

def extrair_top_ips(log_file, top_n):
    """Extrai os top N IPs de destino (dstip) que mais aparecem no arquivo de log."""
    ip_pattern = re.compile(r'dstip=(\d+\.\d+\.\d+\.\d+)')
    ip_counter = Counter()
    
    with open(log_file, "r") as file:
        for line in file:
            match = ip_pattern.search(line)
            if match:
                ip_counter[match.group(1)] += 1
    
    return [ip for ip, _ in ip_counter.most_common(top_n)]

def consultar_shodan(ips, api_key):
    """Consulta os IPs na API do Shodan."""
    shodan_api = shodan.Shodan(api_key)
    resultados = {}
    
    for ip in ips:
        try:
            info = shodan_api.host(ip)
            resultados[ip] = {
                "Organização": info.get("org", "N/A"),
                "ISP": info.get("isp", "N/A"),
                "País": info.get("country_name", "N/A"),
                "Portas": info.get("ports", []),
                "Vulnerabilidades": info.get("vulns", []),
            }
        except shodan.APIError as e:
            resultados[ip] = {"Erro": str(e)}
    
    return resultados

def salvar_resultados(resultados, output_file):
    """Salva os resultados da consulta ao Shodan em um arquivo de texto."""
    with open(output_file, "w") as file:
        for ip, info in resultados.items():
            file.write(f"\nInformações para {ip}:\n")
            for key, value in info.items():
                file.write(f"  {key}: {value}\n")
    print(f"Resultados salvos em {output_file}")

if __name__ == "__main__":
    top_ips = extrair_top_ips(LOG_FILE, TOP_N)
    print(f"Top {TOP_N} IPs mais frequentes encontrados.")
    
    if top_ips:
        shodan_resultados = consultar_shodan(top_ips, SHODAN_API_KEY)
        salvar_resultados(shodan_resultados, OUTPUT_FILE)
