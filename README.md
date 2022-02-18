# SpaceCrypto  Auto Clicker Bot
Também fiz um para Luna Rush ( https://github.com/walterdis/lunarush-bot )

Bot desenvolvido com o intuito de me permitir dormir durante a noite e, poder dar uma volta por ai sem ficar me preocupando com horário ;)

Se o aplicativo lhe ajudar de alguma forma, uma doação para ajudar a pagar a conta de luz sempre é bem vinda ;)

### **Wallet Smart Chain (BNB, LUS, USDT, BUSD)**
0x1F66230C4e98b557D3e55d7d2C047CcbA8E55bD6 
#

# Atenção
O jogo se redimensiona de acordo com a resolução / qualquer modificação na tela da pessoa e isso faz o bot constantemente dar problema, por conta disso, tente a seguinte forma:
- Zoom do browser em 50% (desenvolvi usando o chrome)
- Resolução de 1920x1080
- Tem mais de um monitor e o mouse clica no canto da tela? Experimente desconectar os outros e veja se o problema desaparece
- Não detecta as imagens direito? Tire novamente foto da tela e substitua pelas suas ;)
  

# O que ele faz?
- Conecta na metamask
- Da conta das mensagens popups que aparecem
- Muda a ordenação das naves
- Seleciona as naves disponíveis  para batalha (sem levar em conta raridade)
- Inicia batalha
- Se detectar mais de 1 nave com pouca energia lutando, depois de alguns segundos ele volta para a tela de seleção de naves, remove as com pouca energia e adiciona novas
- Caso não tenha mais naves para luta, ele fica aguardando por alguns minutos antes de tentar novamente

## Obs:
Os movimentos do mouse são aleatórios, por mais que seja permitidos macros no jogo, melhor prevenir ;)

# Requerimentos
### **Tanto o jogo quanto a metamask devem estar em inglês para funcionar corretamente.**
- Python 3.9 (3.10 não funciona)
   - https://www.python.org/downloads/release/python-399/ ou https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe
 - Na instalação, deixe marcado a caixa **"add python  to path"**
 - Execute o arquivo update_requirements.bat ou: Abra o terminal no diretório em que foi baixado o bot e digite ```pip install -r requirements.txt```
 - Digite ```python index.py``` e execute o programa
 
 
*BOT desenvolvido em resolução 1920x1080 (full hd). Caso de problema de detecção de imagens, tente tirar fotos novamente igual as que estão na pasta **target_images***