import discord
from discord.ext import commands
import random

# Permisos para el bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Listas de sugerencias y datos curiosos
sugerencias_reutilizar = [
    "Convierte una botella plástica en una maceta para tus plantas.",
    "Usa frascos de plástico como organizadores para bolígrafos o herramientas pequeñas.",
    "Haz un embudo cortando la parte superior de una botella de plástico.",
    "Crea una lámpara colgante con botellas plásticas y luces LED.",
    "Usa bolsas de plástico para tejer tapetes o bolsos resistentes."
]

datos_reciclaje = [
    "Reciclar una tonelada de plástico puede ahorrar 5,774 kWh de energía.",
    "El plástico tarda entre 100 y 1,000 años en descomponerse.",
    "Las tapas de botellas de plástico son 100% reciclables, pero suelen olvidarse.",
    "Reciclar una botella de plástico puede ahorrar suficiente energía para encender una bombilla durante 3 horas.",
    "Separar los residuos correctamente mejora la calidad del reciclaje."
]

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

#Suggestion to reuse
@bot.command()
async def reutilizar(ctx):
    """Ofrece una sugerencia para reutilizar plásticos."""
    sugerencia = random.choice(sugerencias_reutilizar)
    await ctx.send(f"♻️ **Sugerencia para reutilizar plásticos:** {sugerencia}")

# Curious fact
@bot.command()
async def reciclaje(ctx):
    """Comparte un dato curioso sobre reciclaje."""
    dato = random.choice(datos_reciclaje)
    await ctx.send(f"🌍 **Dato curioso sobre reciclaje:** {dato}")

