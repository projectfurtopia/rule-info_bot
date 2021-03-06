import discord
from discord.ext import commands

TOKEN = ('[REDACTED]')
bot = commands.Bot(command_prefix="r.")

@bot.event
async def on_ready():
    print(bot.user.name + ' has connected to Discord!')
    ready = 0

@bot.command(name='write', aliases=['w'], help='writes the rules (r.w/r.write + main)')
@commands.has_permissions(administrator=True)
async def write_rules(ctx,ruleSet):
    if ruleSet == "main":
        embed=discord.Embed(title="Please read rules carefully", color=0xcf5065)
        embed.set_author(name="PROJECT FURTOPIA RULES")
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="__**1. No hate or harassment of any kind.**__ This includes but is not limited to, hate speech, racism, homophobia, bullying, transphobia, and etc.", value="** **", inline=False)
        embed.add_field(name="__**2. Keep it clean.**__ This means no lewd content in any SFW chat. This includes, but is not limited to, pornography, nudes, yiff, hentai, extreme gore, and etc.", value="** **", inline=False)
        embed.add_field(name="__**3. Open advertisement policy.**__ You are allowed to make any advertisements for personal services such as discord servers, 3D modeling, social media, and etc. However, the advertisements must follow all other rules in the server.", value="**Please refer to other rules for more restrictions.**", inline=False)
        embed.add_field(name="__**4. No illegal content.**__ This server is based in America and must follow the American laws to a tee. Therefore, no posting of anything illegal such as, but not limited to:  human trafficking, bestiality, child pornography, murder, rape, and etc.", value="** **", inline=False)
        embed.add_field(name='__**5. Common sense.**__ Everyone has this, some more than others. If it seems dumb or stupid do not do it. If you are questioning "should I do this?" refer to staff/admins/directors, in that order for an answer. When in doubt ask or just do not do it.', value="** **", inline=False)
        embed.add_field(name="__**6. Reporting.**__ Reports will remain anonymous to the best of our abilities if someone submits a report to the staff. Please refer to staff/admins/directors, in that order for reporting.", value="** **", inline=False)
        embed.add_field(name="__**7.  Authorities.**__ If illegal activities have been reported then it will be acted upon and sent to the proper authorities immediately and I, Alison Blue as will my moderators, will side with the law.", value="** **", inline=False)
        embed.add_field(name="__**8. Discord.**__ When agreeing to abide by these rules you also agree to abide by the Discord official EULA and Terms of Service. You can view the TOS here: https://discord.com/terms.", value="** **", inline=False)
        embed.add_field(name="__**9. Age.**__ You must be 13 years of age to be in the server, however frequently 15 and below will be denied entry to the full server, and 18 and below are restricted from NSFW content.", value="** **", inline=False)
        embed.add_field(name="__**10. Violations.**__ If anyone violates rules they get demoted, if you are only a visitor you will be banned.", value="** **", inline=False)
        embed.set_footer(text="If you have further questions refer to the staff/admins/directors, in that order.\nBy continuing using the server you are accepting these rules.")
        await ctx.send(embed=embed)
    if ruleSet == "roles":
        embed=discord.Embed(title="Go to the below link to get your roles", color=0xcf5065)
        embed.set_author(name="ROLES")
        embed.add_field(name="https://roleypoly.com/s/988546970064945192", value="** **", inline=False)
        embed.set_footer(text="If you have further questions refer to the staff/admins/directors, in that order.")
        await ctx.send(embed=embed)
    await ctx.message.delete()    


@bot.command(name='getImage', aliases=['gi'], help='r.getImage/r.gi  gets server image')
@commands.has_permissions(administrator=True)
async def write_rules(ctx):
    await ctx.send(ctx.guild.icon_url_as(format=None, static_format='png', size=1024))
    
bot.run(TOKEN)
