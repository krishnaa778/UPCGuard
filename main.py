import discord
from discord.ext import commands

# =========================
# CONFIGURATION
# =========================
import os
TOKEN = os.getenv("DISCORD_TOKEN")

# REAL ADMIN USER IDS (never change)
ADMIN_IDS = {
    1364927911232143431,
    939354498638417991,
    966638838468444212,
   1375285022717907045,
  517311966763810836, 
  438745525739847681, 
  800630297251020841, 
  799591860531363890,
 1448660965028528180,
1151148319368822854,
840799346143789126,
1129403660108054598, 
843662067106054184,
1434909782623387831,
768046890888462346,
959479571495923712,
1218079728167288902,
1398725841353048134
}

# Admin display names to protect (lowercase)
ADMIN_NAMES = {
    "upcomers",
    "upc admin",
    "Upcomers",
     "UPC", 
    "Jakub CEO",
"Jakub - Upcomers",
    "Head of customer service",
    "Head of brand reputation",
    "Community Moderator"
}

# Channel ID where alerts will be sent
ALERT_CHANNEL_ID = 1450483855050932355

# =========================
# BOT SETUP
# =========================

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# EVENTS
# =========================

@bot.event
async def on_ready():
    print(f"🛡️ Impersonator Guard is online as {bot.user}")

@bot.event
async def on_member_update(before, after):
    # Ignore real admins
    if after.id in ADMIN_IDS:
        return

    before_name = (before.nick or before.name).lower()
    after_name = (after.nick or after.name).lower()

    # Detect impersonation
    if after_name in ADMIN_NAMES and before_name != after_name:
        channel = after.guild.get_channel(ALERT_CHANNEL_ID)
        if not channel:
            return

        embed = discord.Embed(
            title="🚨 ADMIN IMPERSONATION DETECTED",
            color=discord.Color.red()
        )

        embed.add_field(name="User", value=f"{after} (`{after.id}`)", inline=False)
        embed.add_field(name="Changed Name To", value=after_name, inline=False)
        embed.add_field(name="Server", value=after.guild.name, inline=False)

        await channel.send(embed=embed)

# =========================
# START BOT
# =========================

bot.run(TOKEN)
