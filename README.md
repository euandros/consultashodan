# Consulta Shodan - Análise de IPs com Shodan

![Segmento](https://img.shields.io/badge/Segmento_:-Segurança_da_Informação-blue?style=flat-square) 
![Fase](https://img.shields.io/badge/Fase_:-Estável-green?style=flat-square) 
![Tecnologias](https://img.shields.io/badge/Tecnologias_:-Fortigate,_Python,_Shodan-yellow?style=flat-square) 
![Versão](https://img.shields.io/badge/versão_:-1.0-darkyellow?style=flat-square)

Este repositório contém um script Python que analisa um arquivo de log, identifica os IPs de destino (`dstip`) mais frequentes e consulta informações sobre eles na plataforma Shodan. Os resultados são salvos em um arquivo de texto para análise posterior.

## 📌 Funcionalidades
- Extrai os N IPs de destino (`dstip`) mais frequentes de um arquivo de log.
- Consulta informações detalhadas sobre esses IPs na API do Shodan.
- Salva os resultados em um arquivo de saída (`shodan_results.txt`).

## 🛠️ Requisitos
- Python 3.x
- Biblioteca `shodan`
- Chave de API válida do Shodan

## 🚀 Instalação
1. Clone este repositório:
   ```bash
   git clone [https://github.com/euandros/consultashodan.git]
   cd consultashodan
   ```
2. Instale a biblioteca necessária:
   ```bash
   pip install shodan
   ```
3. Configure sua chave de API do Shodan dentro do script:
   ```python
   SHODAN_API_KEY = "SUA_CHAVE_SHODAN"
   ```

## 📜 Uso
Execute o script da seguinte forma:
```bash
python consulta.py
```
O script processará o arquivo de log especificado e gerará um arquivo `shodan_results.txt` com as informações coletadas.

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para modificá-lo e usá-lo conforme necessário.

