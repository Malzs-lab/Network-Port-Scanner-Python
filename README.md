# Network-Port-Scanner-Python
Scanner básico de portas de rede e Banner Grabber feito em Python.


Uma ferramenta ofensiva de desenvolvida em Python para reconhecimento e mapeamento. O software realiza varreduras automáticas em uma grade de portas corporativas críticas e faz a extração ativa de banners para identificar sistemas operacionais e versões de serviços rodando no alvo.

 Utilidades e Funcionalidades
* Varredura Multidomínio: Suporta tanto endereços IP quanto Hostnames (URLs), realizando a resolução de nomes (DNS) de forma automatizada.
* Mapeamento de Portas Críticas (12 Alvos): Configurado para checar serviços essenciais de redes e infraestrutura (SSH, HTTP, HTTPS), acesso remoto (RDP, Telnet) e bancos de dados (MSSQL `1433`, MySQL `3306`, PostgreSQL `5432`).
* Banner Grabbing Ativo: Conecta-se às portas abertas para capturar as strings de boas-vindas dos serviços, expondo versões exatas de softwares (essencial para análise de vulnerabilidades).
* Interface Gráfica: Painel interativo construído em `tkinter` com design customizado em modo escuro e saída de dados simulando um terminal hacker em tempo real.
* Blindagem Contra Lag (Multi-threading):O motor de varredura e as requisições de rede rodam de forma assíncrona usando a biblioteca `threading`. Isso garante que a interface gráfica permaneça 100% lisa mesmo durante testes internacionais de longa distância.
* Validação de Entrada Sólida: Tratamento de exceções robusto via `port.gaierror` que impede a quebra do software caso o usuário digite um IP inválido ou uma URL inexistente.

 Tecnologias Utilizadas
* Python 3 (Linguagem base)
* Socket (Comunicação de rede em baixo nível e handshakes TCP)
* Threading (Execução em segundo plano)
* Tkinter (Design de interface de usuário)

 Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado no sistema.
2. Baixe o script `scanner_visual.py` deste repositório.
3. Execute o arquivo através do seu terminal ou IDE:
   ```bash
   python scanner_visual.py
   ```
4. Digite o IP ou Hostname do alvo na caixa de entrada (o site de testes legítimo `scanme.nmap.org` já vem preenchido por padrão).
5. Clique em Iniciar Scan e acompanhe a varredura cadenciada sendo desenhada no painel!

🚨 Aviso Legal (Disclaimer)
Este projeto foi desenvolvido estritamente para fins educacionais e testes de invasão autorizados (Hacking Ético). O uso desta ferramenta contra alvos sem permissão prévia é de total responsabilidade do usuário. Utilize sempre ambientes controlados ou alvos de teste públicos como o fornecido pelo projeto Nmap. Caso utilizado de forma maliciosa, eu Malzs, declaro que eu não tenho nenhum envolvimento e tais ações são responsabilidade do usuário e somente deste.
