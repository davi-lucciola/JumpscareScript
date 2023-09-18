# JumpScare Script

## Como utilizar

Você precisa configurar no `.env` as seguintes variavéis: 

- Horario do Jumpscare (Formato: HH:MM) - JUMPSCARE_TIME
- Path (Absoluto ou Relativo) da imagem - IMAGE_PATH
- Path (Absoluto ou Relativo) do som - SOUND_PATH
- Duração do som em segundos. - SOUND_SECONDS

OBS: está programado para executar na proxima vez que o PC chegar na hora que você colocar (Exemplo: se for 13:00 da tarde e vc colocar 12:00 horas, irá executar somente no dia seguinte).

Caso esteja vazio ele vai programar para daqui a um minuto.

### Execute o script abaixo

- Windows:
> `python -m venv .venv && .venv\Scripts\activate && pip install --upgrade setuptools wheel && pip install -r requirements.txt && pythonw main.pyw`


OBS: para Linux e Mac é só substituir o "python" pelo "python3"

### ou faça passo a passo:

- Instale as depêndencias

1. > `python -m venv .venv`

2. > `.venv\Scripts\activate`

3. > `pip install --upgrade setuptools wheel`

4. > `pip install -r requirements.txt`

- Executando o script

5. > `pythonw main.pyw`